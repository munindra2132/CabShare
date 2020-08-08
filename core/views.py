from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Trip, MyTrips, MyTrip
# Create your views here.


# def trip_list(request):
#     context = {
#         'trips': Trip.objects.all()
#     }
#     return render(request, "list.html", context)


class HomeView(ListView):
    model = Trip
    template_name = "list.html"


class TripDetailView(DetailView):
    model = Trip
    template_name = "trip.html"


def about(request):
    return render(request, "about.html")


def add_to_list(request, slug):
    trip = get_object_or_404(Trip, slug=slug)


def yourtrips(request):
    return render(request, "yourtrips.html")


def search(request):
    return render(request, "search.html")
