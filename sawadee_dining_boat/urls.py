from django.contrib import admin
from django.urls import path, include
from reservations import views as index_views
from django.conf.urls import handler404, handler500, handler403, handler400
from django.shortcuts import render

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('reservations/', include('reservations.urls', namespace='reservations')),
    path('', include('info.urls')), 
    path('admin/', admin.site.urls),
]
# Custom 404 Error Page
def custom_404_view(request, exception):
    return render(request, "404.html", status=404)

# Custom 403 Forbidden Error Page
def custom_403_view(request, exception):
    return render(request, "403.html", status=403)

# Custom 500 Internal Server Error Page
def custom_500_view(request):
    return render(request, "500.html", status=500)

# Custom 400 Bad Request Error Page
def custom_400_view(request, exception):
    return render(request, "400.html", status=400)

# Assign error handlers
handler404 = custom_404_view
handler500 = custom_500_view
handler403 = custom_403_view
handler400 = custom_400_view