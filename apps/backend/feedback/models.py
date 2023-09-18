from django.db import models

from django.utils.translation import gettext_lazy as _

# Create your models here.
class Feedback(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    text = models.TextField(_("Text"), max_length=2000)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'feedbacks'
        verbose_name_plural = ' Feedback'