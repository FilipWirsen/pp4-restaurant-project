from django.shortcuts import render, redirect
from .forms import MakeReservationForm
from .models import Reservation, Table
from django.contrib import messages
import datetime
from django.views import View
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    """
    Returns home page
    """
    return render(request, 'home.html')


def menu(request):
    """
    Returns menu page
    """
    return render(request, 'menu.html')


def check_availability(party_size, date, start_time):
    """
    Checks if booking time is availible
    """
    bookings_before_time = start_time - 105
    bookings_after_time = start_time + 105
    if party_size <= 2:
        table_size = 2
    elif party_size >= 3:
        table_size = 4
    get_bookings_before = Reservation.objects.filter(
        book_date=date, table__table_size__contains=table_size, book_time__range=(
            bookings_before_time, start_time))
    get_bookings_after = Reservation.objects.filter(
        book_date=date, table__table_size__contains=table_size, book_time__range=(
            start_time, bookings_after_time))
    if get_bookings_before.count() == 5 or get_bookings_after.count() == 5:
        return False, False
    else:
        tables = Table.objects.filter(table_size=table_size)
        for table in tables:
            if not Reservation.objects.filter(book_date=date, book_time__range=(bookings_before_time, bookings_after_time), table=table).exists():
                availible_table = table
                return availible_table, True
            else:
                return False, False

@login_required
def reserve_table(request):
    """
    Reserve table based on MakeReservationForm
    """
    if request.method == 'POST':
        form = MakeReservationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            data = form.cleaned_data

            post.size = data['party_size']
            post.date = data['book_date']
            post.time = data['book_time']
            post.end_time = post.time + 120

            if post.date < datetime.date.today():
                messages.error(
                    request, "Date has to be today or future, please choose another date")
                return render(
                    request, 'reservation/reservation.html', {'form': form})

            availible_table, availible = check_availability(
                post.size, post.date, post.time)

            if availible:
                post.table = availible_table
                post.save()
                booking = post
                return render(
                    request, 'reservation/reservation_details.html', {'booking': booking})
            else:
                form = MakeReservationForm()
                messages.error(
                    request, "Time is not availible, please choose another")
                return render(
                    request, 'reservation/reservation.html', {'form': form})
    else:
        form = MakeReservationForm()
        return render(request, 'reservation/reservation.html', {'form': form})


class ReservationDetail(View):

    def get(self, request, *args, **kwargs):
        user = request.user
        reservations = Reservation.objects.filter(user=user)
        return render(
            request,
            'reservation/manage_reservations.html',
            {
                'reservations': reservations
            })


@login_required
def update_reservation(request, reservation_id):
    """
    Function to update reservation
    """
    reservation = Reservation.objects.filter(pk=reservation_id).first()
    form = MakeReservationForm(request.POST or None, instance=reservation)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        data = form.cleaned_data

        post.size = data['party_size']
        post.date = data['book_date']
        post.time = data['book_time']
        post.end_time = post.time + 120

        if post.date < datetime.date.today():
            messages.error(
                request, "Date has to be today or future, please choose another date")
            return render(
                request, 'reservation/update_reservation.html', {'form': form})

        availible_table, availible = check_availability(
            post.size, post.date, post.time)

        if availible:
            post.table = availible_table
            post.save()
            booking = post
            return render(
                request, 'reservation/reservation_details.html', {'booking': booking})
        else:
            form = MakeReservationForm()
            messages.error(
                request, "Time is not availible, please choose another")
            return render(
                request, 'reservation/update_reservation.html', {'form': form})
    else:
        messages.error(request, "Please enter all fields")
        return render(
            request, 'reservation/update_reservation.html', {'form': form, 'reservation': reservation})


@login_required
def delete_reservation(request, reservation_id):
    """
    View to delete reservation
    """
    reservation = Reservation.objects.get(pk=reservation_id)

    if request.method == "POST":
        reservation.delete()
        return render(request, 'home.html')
    
    return render(
        request, 'reservation/delete_reservation.html', {'reservation': reservation})