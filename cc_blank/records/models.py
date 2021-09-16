from django.db import models
from django.utils.translation import gettext_lazy as _
from .abstract_models import AbstractRecord

# Create your models here.
class Record(AbstractRecord):
    class RecordType(models.TextChoices):
        MOISTURE_CONTENT = "MOISTURE_CONTENT", _("Moisture Content")
        SIZE_CHECK = "SIZE_CHECK", _("Size Check")
        KILN_TIME = "KILN_TIME", _("Kiln Time")

    record_type = models.CharField(
        _("Record Types"), default=RecordType.MOISTURE_CONTENT, max_length=20,
        choices=RecordType.choices)

    moisture_content = models.DecimalField(
        _("Moisture Content"), decimal_places=2, max_digits=12, null=True)

    measured_width = models.PositiveIntegerField(_("Measured Width(mm)"), null=True) # unit mm
    measured_depth = models.PositiveIntegerField(_("Measured Depth(mm)"), null=True)

    kiln_start_time = models.DateTimeField(_("Kiln Start Time"), null=True)
    kiln_finish_time = models.DateTimeField(_("Kiln Finish Time"), null=True)

    @property
    def kiln_duration(self):
        if self.kiln_finish_time and self.kiln_start_time:
            kiln_duration = self.kiln_finish_time - self.kiln_start_time
            return kiln_duration.total_seconds() / 3600 # in hours
        return None