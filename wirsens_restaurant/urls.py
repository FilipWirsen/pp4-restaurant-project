from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reservation', views.reserve_table, name='reservation'),
    path('manage-reservation', views.ReservationDetail.as_view(), name='manage-reservation'),
    path('update-reservation/<int:reservation_id>', views.UpdateReservation.as_view(), name='update-reservation'),
]