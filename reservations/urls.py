from . import views
from django.urls import path


urlpatterns = [
    path('', views.ReservationListView.as_view(), name='reservation_list')
]




