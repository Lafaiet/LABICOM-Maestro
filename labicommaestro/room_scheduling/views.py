from django.shortcuts import render
from django.shortcuts import redirect
from models import Reservation, Room
from django.db.models import Q
from django.contrib.auth.decorators import login_required
import datetime
from itertools import chain

# Create your views here.


def main_page_view(request):

    today_date = datetime.date.today()
    str_date = today_date.isoformat().replace('-', '/')
    return redirect('/reservas/%s'%(str_date))

@login_required()
def request_reservation_view(request):

    rooms = Room.objects.all()

    if request.method == 'POST':
        return render(request, 'reservation_page.html', {'rooms' : rooms, 'status': 'error'})

    return render(request, 'reservation_page.html', {'rooms' : rooms})


def reservation_day_view(request, year, month, day):
    #year, month, day = reservation_date.split('/')
    date = datetime.date(int(year), int(month), int(day))
    reservations1 = Reservation.objects.filter(event_date=date).filter(confirmed=True)

    reservations2 =  Reservation.objects.filter(is_permanent=True).filter(weekday=date.weekday()).filter(confirmed=True)

    reservations = list(chain(reservations1, reservations2))

    for reservation in reservations:
        if reservation.is_permanent:
            reservation.event_name += "*"

    return render(request, 'reservas.html', {'reservations' : reservations, 'date' : date})



def profile_view(request):

    return redirect("main_page")

def contact_view(request):

    if request.method == 'POST':
        return render(request, 'contact.html', {'status': 'error' })

    return render(request, 'contact.html')

def calendar_view(request):
    return render(request, 'calendar.html', {})

def register_user_view(request):
    if request.method == 'POST':
        return render(request, 'register.html', {'status': 'error' })
    return render(request, 'register.html')

def test(request):
    return render(request, 'register.html')
