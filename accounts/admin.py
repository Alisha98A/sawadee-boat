from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from allauth.account.utils import send_email_confirmation
from .models import Profile


class CustomUserAdmin(UserAdmin):
    """Custom admin to handle user registration and email confirmation."""

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (None, {"fields": ("email",)}),  # Ensure email is included
    )

    def save_model(self, request, obj, form, change):
        """Override save_model to send email confirmation for new users."""
        is_new_user = obj._state.adding  # Check if user is newly created
        super().save_model(request, obj, form, change)

        if is_new_user:
            obj.is_active = False  # Deactivate new users
            obj.save()
            send_email_confirmation(
                request, obj
            )  # Send confirmation email


# Unregister default User admin and register the custom admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Admin panel customization for user profiles."""

    list_display = (
        "user",
        "first_name",
        "last_name",
        "phone_number",
        "address",
    )
