from django.shortcuts import render
from django.shortcuts import redirect
from models import Reservation
from django.contrib.auth.decorators import login_required

# Create your views here.


def main_page_view(request):

    reservations = Reservation.objects.all()

    return render(request, 'main_page.html', {'reservations' : reservations})

@login_required()
def request_reservation_view(request):

    return render(request, 'reservation_page.html')


def profile_view(request):

    return redirect("main_page")
