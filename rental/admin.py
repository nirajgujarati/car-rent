from django.contrib import admin
from django.contrib import admin
from .models import User, CarOwner, Car  # Import all models

# Register User Model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "mobile_number", "city", "created_at")
    search_fields = ("full_name", "email", "mobile_number")
    list_filter = ("city", "state", "country")

# Register CarOwner Model
@admin.register(CarOwner)
class CarOwnerAdmin(admin.ModelAdmin):
    list_display = ("username", "password", "created_at")  # Display only relevant fields
    search_fields = ("username",)


from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "number_plate", "hourly_rate", "daily_rate", "with_driver", "status", "created_at")
    search_fields = ("name", "company", "number_plate")
    list_filter = ("status", "with_driver", "company")
    ordering = ("-created_at",)


# # Register Booking Model
# @admin.register(Booking)
# class BookingAdmin(admin.ModelAdmin):
#     list_display = ("user", "car", "start_date", "end_date", "status")
#     search_fields = ("user__full_name", "car__name")
#     list_filter = ("status",)


# Register your models here.
