# records/tables.py
import django_tables2 as tables
from .models import Record
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

class RecordTable(tables.Table):
    delete = tables.TemplateColumn(verbose_name=_(''),
                                template_name='records/components/delete_button.html',
                                orderable=False)
    class Meta:
        model = Record
        template_name = "django_tables2/bootstrap.html"
        fields = ("id", "record_type", "record_pass", "record_comments", "action" )

    def render_id(self, value):
        return format_html("<a href=\"/records/edit/{}/\">#{}</a>", value, value)

    def render(self, record):
            return format_html("<button onclick=\"windows.location.href=\"/records/edit/{}/\"\">#{}</button>", record.id, "Delete")
