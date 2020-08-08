from django.urls import path
from .views import (
    HomeView,
    TripDetailView,
    yourtrips,
    search,
    about
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='trip-list'),
    path('trip/<slug>/', TripDetailView.as_view(), name='trip'),
    path('yourtrips/', yourtrips, name='yourtrips'),
    path('search/', search, name='search'),
    path('about/', about, name="about")
]
