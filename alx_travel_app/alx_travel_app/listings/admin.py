from django.contrib import admin
from .models import Property, Booking, Review


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'property_type', 'location', 'price_per_night', 'is_available', 'created_at']
    list_filter = ['property_type', 'is_available', 'location']
    search_fields = ['name', 'location', 'description']
    list_editable = ['is_available']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'property', 'check_in_date', 'check_out_date', 'status', 'total_price']
    list_filter = ['status', 'check_in_date']
    search_fields = ['user__username', 'property__name']
    list_editable = ['status']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'property', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['user__username', 'property__name', 'comment']
