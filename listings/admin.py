from django.contrib import admin
from django.db import models
from django import forms
from django.utils.html import format_html
from django.urls import reverse
from django.contrib import messages
from .models import Listing, ListingPhoto
from django.forms.models import BaseInlineFormSet
from utils import get_html_link

# Register your models here.
class ListingPhotoAdminFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()
        model_forms = [form for form in self.forms if form.cleaned_data]
        if len(model_forms) == 1:
            self.forms[0].cleaned_data['is_main'] = True
        elif len(model_forms) > 1:
            main_imgs = [form for form in model_forms if form.is_valid() \
                    and form.cleaned_data.get('is_main', False)]
            if len(main_imgs) != 1:
                error_message = "Missing main image" if not main_imgs else "Only one main image allowed"
                raise forms.ValidationError(error_message)
            

class ListingPhotoAdmin(admin.TabularInline):
    model = ListingPhoto
    formset = ListingPhotoAdminFormset
    fields = ['photo','photo_preview', 'is_main']
    readonly_fields = ['photo_preview']
    extra = 6

    def get_max_num(self, request, obj=None, **kwargs):
        if obj:
            return 6 - obj.photos.count()
        return 6

    def photo_preview(self, obj):
        if obj.photo.url:
            return format_html(f"<img src='{obj.photo.url}' height='100' width='100'/>")
        return None

    def get_queryset(self, request):
        qs = super(ListingPhotoAdmin, self).get_queryset(request)
        return qs.order_by('-is_main')

class ListingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Default is street + city + zip'
        self.fields['is_published'].widget.attrs['checked'] = True
    
    class Meta:
        model = Listing
        fields = [
            'realtor', 'listing_type', 'title', 'street', 'city', 'state', 'zipcode', 'unit_number', 
            'description', 'price', 'bedrooms', 'bathrooms', 'garage', 'lot_size', 'sqft', 'is_published',
        ]

    def clean(self):
        if self.cleaned_data['listing_type'] in ['APT', 'CONDO'] and not self.cleaned_data['unit_number']:
            raise forms.ValidationError("Apartments and condos must specify a unit number.")
        elif self.cleaned_data['listing_type'] == 'HOUSE' and self.cleaned_data['unit_number']:
            raise forms.ValidationError("Houses cannot have a unit number.")
        return self.cleaned_data

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):

    def realtor_name(self, obj):
        return get_html_link(obj, obj.realtor.id, obj.realtor.name)
        

    formfield_overrides = {
        models.ForeignKey: {'widget': forms.Select},
    }

    form = ListingForm
    list_display = ['id', 'title', 'is_published', 'price', 'list_date', 'realtor_name']
    list_filter = ('realtor__name','state',)
    readonly_fields = ['list_date', 'latitude', 'longitude']
    
    inlines = [ListingPhotoAdmin]
    ordering = ('-list_date',)    
    list_per_page = 15 

    def save_model(self, request, obj, form, change):
        # if not obj.latitude or not obj.longitude:
        #     messages.warning(request, "Warning: Could not validate the address you provided.")
        super(ListingAdmin, self).save_model(request, obj, form, change)

    