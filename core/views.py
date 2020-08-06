from django.shortcuts import render
from .models import Trip
# Create your views here.


def trip_list(request):
    context = {
        'trips': Trip.objects.all()
    }
    return render(request, "list.html", context)


def yourtrips(request):
    return render(request, "yourtrips.html")


def search(request):
    return render(request, "search.html")
