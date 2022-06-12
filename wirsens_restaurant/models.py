from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Table(models.Model):
    """
    Model for restaurant tables that specifies the table size
    """
    TableID = models.AutoField(primary_key=True)
    table_size = models.IntegerField()

    def __str__(self):
        return f"Table Number: {self.TableID}"


class Reservation(models.Model):
    """
    Model for storing reservations.
    Each time choice key is the amount of minutes until the time 'value'
    """
    reservation_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    party_size = models.IntegerField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    book_date = models.DateField(default=timezone.now)
    TIME_CHOICES = [
        (1050, '17:30'),
        (1065, '17:45'),
        (1080, '18:00'),
        (1095, '18:15'),
        (1110, '18:30'),
        (1125, '18:45'),
        (1140, '19:00'),
        (1155, '19:15'),
        (1170, '19:30'),
        (1185, '19:45'),
        (1200, '20:00'),
        (1215, '20:15'),
        (1230, '20:30'),
        (1245, '20:45'),
        (1260, '21:00'),
        (1275, '21:15'),
        (1290, '21:30'),
        (1305, '21:45'),
        (1320, '22:00'),
    ]
    book_time = models.IntegerField(choices=TIME_CHOICES)
    end_time = models.IntegerField(blank=True)
