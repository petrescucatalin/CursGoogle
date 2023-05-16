from django.contrib import admin
from .models import Company, Location

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'location', 'is_active')
    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    make_active.short_description = "Mark selected companies as active"

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_inactive.short_description = "Mark selected companies as inactive"

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Add any other fields you want to display
