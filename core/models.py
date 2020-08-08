from django.conf import settings
from django.db import models
from django.shortcuts import reverse
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
    slug = models.SlugField()

    def __str__(self):
        return self.organizer

    def get_absolute_url(self):
        return reverse("core:trip", kwargs={
            'slug': self.slug
        })


class MyTrips(models.Model):
    pass


class MyTrip(models.Model):
    pass
