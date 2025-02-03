from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf.urls import (
    handler404, handler500, handler403, handler400
)
from reservations import views as index_views

urlpatterns = [
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("allauth.urls")),
    path(
        "reservations/",
        include("reservations.urls", namespace="reservations"),
    ),
    path("", include("info.urls")),
    path("admin/", admin.site.urls),
]


# --------------------------------------
# Custom Error Handlers
# --------------------------------------


def custom_404_view(request, exception):
    """Render the custom 404 error page."""
    return render(request, "404.html", status=404)


def custom_403_view(request, exception):
    """Render the custom 403 Forbidden error page."""
    return render(request, "403.html", status=403)


def custom_500_view(request):
    """Render the custom 500 Internal Server Error page."""
    return render(request, "500.html", status=500)


def custom_400_view(request, exception):
    """Render the custom 400 Bad Request error page."""
    return render(request, "400.html", status=400)


# Assign error handlers
handler404 = custom_404_view
handler500 = custom_500_view
handler403 = custom_403_view
handler400 = custom_400_view
