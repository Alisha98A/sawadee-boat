from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from allauth.account.utils import send_email_confirmation
from .models import Profile

class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (None, {"fields": ("email",)}),
    )

    def save_model(self, request, obj, form, change):
        is_new_user = obj._state.adding  
        super().save_model(request, obj, form, change)
        if is_new_user:
            obj.is_active = False  
            obj.save()
            send_email_confirmation(request, obj)  

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone_number', 'address')