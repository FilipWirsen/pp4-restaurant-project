from django.forms import ModelForm
from .models import Reservation


class MakeReservationForm(ModelForm):
    """
    Form for Reservation model
    """

    class Meta:
        model = Reservation
        fields = ('party_size', 'book_date', 'book_time')
        exclude = ('table', 'end_time')
