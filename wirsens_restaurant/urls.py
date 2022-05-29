from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reservation', views.reserve_table, name='reservation'),
    path('manage-reservation', views.ReservationDetail.as_view(), name='manage_reservation')
]