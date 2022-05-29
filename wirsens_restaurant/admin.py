from django.contrib import admin
from .models import Reservation, Table


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_filter = ('book_date', 'book_time')
    list_display = ('user', 'table', 'book_date', 'book_time')
    search_fields = ['user']


admin.site.register(Table)