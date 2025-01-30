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

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """Admin panel settings for the MenuItem model."""
    list_display = ("menu", "category")
    inlines = [ItemInline]

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "menu_item", "price")
    search_fields = ("name",)