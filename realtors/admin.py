from django.contrib import admin
from django.utils.html import mark_safe
from .models import Realtor
from contacts.models import Contact
from utils import get_html_link

# Register your models here. 
class ContactInline(admin.TabularInline):
    extra = 0
    max_num = 0
    can_delete = False
    model = Contact
    fields = ['link', 'listing', 'name', 'email', 'contact_date', 'responded']
    readonly_fields = ['link', 'listing', 'name', 'email', 'contact_date']
    verbose_name_plural = 'Inquiries'

    def link(self, obj):
        return get_html_link(obj, obj.pk, obj.pk)

@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'hire_date']
    readonly_fields = ('img_preview',)
    ordering = ['-hire_date']
    inlines = [ContactInline]

    def img_preview(self, obj):
        return mark_safe(f"<img width='400' height='300' src='{obj.photo.url}' />")

        