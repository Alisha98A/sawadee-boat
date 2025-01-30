from django.contrib import admin
from .models import Menu, MenuItem, Item

class MenuItemInline(admin.TabularInline):
    """Allows MenuItems to be edited directly inside the Menu admin page."""
    model = MenuItem
    extra = 1

admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Item)