from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.backend.room.models import *


# Create your models here.

class Booking(models.Model):
    first_name = models.CharField(_("First Name"), max_length=200)
    last_name = models.CharField(_("Last Name"), max_length=200)
    email = models.CharField(_("Email"), max_length=200)
    phone = models.CharField(_("Phone"), max_length=200)
    booking_date = models.DateField(_('Booking Date'))
    arrival_date = models.DateField(_('Arrival Date'))
    no_of_people = models.CharField(_("No Of People"), max_length=200)
    type = models.ForeignKey(RoomType, verbose_name=_('Room Type'), on_delete=models.CASCADE)
    room = models.ForeignKey(Room, verbose_name=_('Room'), on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        db_table = 'booking'
        verbose_name_plural = 'Booking'