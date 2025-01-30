from django.urls import path
from . import views
from .views import menu_view


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path("menu/", menu_view, name="menu"),
]