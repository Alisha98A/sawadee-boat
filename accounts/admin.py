from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Profile

class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (None, {"fields": ("email",)}),  # Ensure email is required when creating a user
    )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone_number', 'address')