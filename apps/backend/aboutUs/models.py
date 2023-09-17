from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class aboutUs(models.Model):
    file = models.FileField(_("Title"), upload_to='aboutUs', default='default/img.png')
    title = models.CharField(_("Title"), max_length=200)
    about = models.TextField(_("About"), max_length=2000)
    status = models.BooleanField(_('Status'), default=True)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'about_us'
        verbose_name_plural = 'About Us'

