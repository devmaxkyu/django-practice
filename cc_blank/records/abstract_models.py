from django.db import models
from django.utils.translation import gettext_lazy as _

class AbstractRecord(models.Model):
    record_pass = models.BooleanField(_("Pass"), default=False)
    record_comments = models.CharField(_("Comments"), max_length=500, blank=True)

    class Meta:
        abstract = True
        app_label = 'records'
        verbose_name = _('Record')
        verbose_name_plural = _('Records')

    def __str__(self):
        return f"#{self.pk}"