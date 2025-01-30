from django.contrib import admin
from .models import Menu, MenuItem, Item

class MenuItemInline(admin.TabularInline):
    """Allows MenuItems to be edited directly inside the Menu admin page."""
    model = MenuItem
    extra = 1

class ItemInline(admin.TabularInline):
    """Allows Items to be edited directly inside the MenuItem admin page."""
    model = Item
    extra = 1

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Admin panel settings for the Menu model."""
    list_display = ("name", "is_active")
    list_filter = ("is_active",)
    inlines = [MenuItemInline]
    actions = ["set_active_menu"]

    def set_active_menu(self, request, queryset):
        """Ensure only one menu is active at a time."""
        if queryset.count() > 1:
            self.message_user(request, "You can only activate one menu at a time.", level="error")
        else:
            Menu.objects.update(is_active=False)  
            queryset.update(is_active=True)  
            self.message_user(request, "Selected menu is now active.")

    set_active_menu.short_description = "Set as Active Menu"

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """Admin panel settings for the MenuItem model."""
    list_display = ("menu", "category")
    inlines = [ItemInline]

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "menu_item", "price")
    search_fields = ("name",)