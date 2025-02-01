from django.urls import path
from . import views
from .views import menu_view, set_sail_view, staff_menu_view, add_menu, edit_menu, delete_menu, no_access


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path("menu/", menu_view, name="menu"),
    path("set-sail/", set_sail_view, name="set_sail"),
    # Menu Management
    path("staff/menu/", views.staff_menu_view, name="staff_menu"),
    path("staff/menu/add/", views.add_menu, name="add_menu"),
    path("staff/menu/edit/<int:menu_id>/", views.edit_menu, name="edit_menu"),
    path("staff/menu/delete/<int:menu_id>/", views.delete_menu, name="delete_menu"),
    path("staff/menu/set-active/<int:menu_id>/", views.set_active_menu, name="set_active_menu"),

    # Menu Item (Categories) Management
    path("staff/menu-item/add/", views.add_menu_item, name="add_menu_item"),
    path("staff/menu-item/edit/<int:menu_item_id>/", views.edit_menu_item, name="edit_menu_item"),
    path("staff/menu-item/delete/<int:menu_item_id>/", views.delete_menu_item, name="delete_menu_item"),

    # Item (Dishes) Management
    path("staff/item/add/", views.add_item, name="add_item"),
    path("staff/item/edit/<int:item_id>/", views.edit_item, name="edit_item"),
    path("staff/item/delete/<int:item_id>/", views.delete_item, name="delete_item"),

    # No Access Page
    path("no-access/", views.no_access, name="no_access"),
]
