from django.shortcuts import render
from models import Reservation

# Create your views here.


def main_page_view(request):



    reservations = Reservation.objects.all()

    return render(request, 'main_page.html', {'reservations' : reservations})
