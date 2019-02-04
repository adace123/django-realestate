from django.contrib import admin
from .models import Contact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['pk', 'listing', 'realtor_name', 'contact_date']
    readonly_fields = ['name', 'email', 'listing', 'realtor_name', 'message', 'contact_date']

    def realtor_name(self, obj):
        return obj.listing.realtor.name

    def delete_model(self, request, queryset):
        for obj in queryset:
            admin.ModelAdmin.message_user

