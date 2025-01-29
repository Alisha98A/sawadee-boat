from django.contrib import admin
from django.urls import path, include
from reservations import views as index_views

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('reservations/', include('reservations.urls', namespace='reservations')),
    path('', include('info.urls')), 
    path('admin/', admin.site.urls),
]