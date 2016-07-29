from django.shortcuts import render
from django.shortcuts import redirect
from models import Reservation, Room
from django.contrib.auth.decorators import login_required

# Create your views here.


def main_page_view(request):

    reservations = Reservation.objects.all()

    return render(request, 'main_page.html', {'reservations' : reservations})

@login_required()
def request_reservation_view(request):

    rooms = Room.objects.all()

    if request.method == 'POST':
        return render(request, 'reservation_page.html', {'rooms' : rooms, 'status': 'error'})

    return render(request, 'reservation_page.html', {'rooms' : rooms})


def profile_view(request):

    return redirect("main_page")

def contact_view(request):

    if request.method == 'POST':
        return render(request, 'contact.html', {'status': 'error' })

    return render(request, 'contact.html')

def calendar_view(request):
    return render(request, 'calendar.html', {})

def test(request):
    return render(request, 'login2.html')
