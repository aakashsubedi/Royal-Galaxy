from django.db import models
from django.utils.translation import gettext_lazy as _



# Create your models here.
class Footer(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    value = models.CharField(_("Value"), max_length=200)
    status = models.BooleanField(_('Status'), default=True)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)

    def __str__(self):
        return self.value

    class Meta:
        db_table = 'footer'
        verbose_name_plural = ' Footer '
