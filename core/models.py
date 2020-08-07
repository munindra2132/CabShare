from django.db import models

# Create your models here.


class Trip(models.Model):
    places = [
        ('IITG', 'IITG'),
        ('RAILWAY STATION GUWAHATI', 'RAILWAY STATION GUWAHATI'),
        ('RAILWAY STATION KAMAKHYA', 'RAILWAY STATION KAMAKHYA'),
        ('AIRPORT', 'AIRPORT'),
    ]
    src = models.CharField(
        max_length=50,
        choices=places,
        null=False,
        blank=False,
    )
    dest = models.CharField(
        max_length=50,
        choices=places,
        null=False,
        blank=False,
    )
    organizer = models.CharField(max_length=50)
    journey_date = models.DateTimeField(
        auto_now=False, auto_now_add=False, blank=False, null=False)

    def __str__(self):
        return self.organizer


class MyTrips(models.Model):
    pass


class MyTrip(models.Model):
    pass
