from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu', views.menu, name='menu'),
    path('reservation', views.reserve_table, name='reservation'),
    path('manage-reservation', views.ReservationDetail.as_view(), name='manage-reservation'),
    path('update-reservation/<int:reservation_id>', views.update_reservation, name='update-reservation'),
    path('delete-reservation/<int:reservation_id>', views.delete_reservation, name='delete-reservation'),
]
