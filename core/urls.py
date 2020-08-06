from django.urls import path
from .views import trip_list

app_name = 'core'

urlpatterns = [
    path('', trip_list, name='trip-list')
]
