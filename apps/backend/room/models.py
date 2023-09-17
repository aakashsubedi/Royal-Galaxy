from django.db import models
from django.utils.translation import gettext_lazy as _



# Create your models here.
class RoomType (models.Model):
    title = models.CharField(_("Title"), max_length=200)
    status = models.BooleanField(_('Status'), default=True)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)



    def __str__(self):
        return self.title

    class Meta:
        db_table = 'room_types'
        verbose_name_plural = 'Room Type'

class Room (models.Model):
    image = models.ImageField(_("Image"), upload_to='room', default='default/img.png')
    title = models.CharField(_("Title"), max_length=200)
    text = models.TextField(_("Text"), max_length=2000)
    status = models.BooleanField(_('Status'), default=True)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    price=models.IntegerField(_('Price'), default=10)
    position=models.IntegerField(_('Position'), null=True, blank=True)
    type=models.ForeignKey(RoomType, verbose_name=_('Room Type'),on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'room'
        verbose_name_plural = 'Room'