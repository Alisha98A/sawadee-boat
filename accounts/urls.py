from django.urls import path, include
from . import views
from .views import profile_view, ProfileUpdateView, delete_account
from django.views.generic import TemplateView 


urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='edit_profile'), 
    path("delete-account/", delete_account, name="delete_account"),
]