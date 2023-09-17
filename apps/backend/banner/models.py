from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Banner(models.Model):
    image = models.ImageField(_("Image"), upload_to='banners', default='default/img.png')
    status = models.BooleanField(_('Status'), default=True)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)

    class Meta:
        db_table = 'banners'
        verbose_name_plural = ' Banners'
