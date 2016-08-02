from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.


class Room(models.Model):
    room_name = models.CharField(primary_key=True, max_length=400)
    room_capacity = models.IntegerField()

    def __unicode__(self):
		return '%s' % self.room_name


class Reservation(models.Model):
    event_name = models.CharField(max_length=400)
    user_requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.ForeignKey(Room)
    event_date = models.DateField(null=True, blank = True)

    is_permanent = models.BooleanField(default = False)

    weekdays_choices = ((0, 'monday'), (1, 'tuesday'),
                        (2, 'wednesday'), (3, 'thursday'),
                        (4, 'friday'), (5, 'saturday'),
                        (6, 'sunday'))
    weekday = models.IntegerField(null = True, blank  = True, choices = weekdays_choices)
