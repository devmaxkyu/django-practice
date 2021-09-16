from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Record
from crispy_forms.helper import FormHelper

class RecordsFilterForm(forms.Form):
    record_type = forms.ChoiceField(label=_('Type'), choices=[(None, "--Type--")] + Record.RecordType.choices, required=False)
    record_pass = forms.ChoiceField(label=_('Pass'), choices=((None, "--Pass--"), (True, True), (False, False)), required=False)

    def __init__(self, *args, **kwargs):
        super(RecordsFilterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

class MoistureContentRecordCreateForm(forms.Form):
    record_pass = forms.BooleanField(label=_("Pass"), required=False)
    record_comments = forms.CharField(label=_("Comments"), required=False, max_length=500)
    moisture_content = forms.FloatField(required=True)

class SizeCheckRecordCreateForm(forms.Form):
    record_pass = forms.BooleanField(label=_("Pass"), required=False)
    record_comments = forms.CharField(label=_("Comments"), required=False, max_length=500)
    measured_width = forms.IntegerField(required=True)
    measured_depth = forms.IntegerField(required=True)

class KilnTimeRecordCreateForm(forms.Form):
    record_pass = forms.BooleanField(label=_("Pass"), required=False)
    record_comments = forms.CharField(label=_("Comments"), required=False, max_length=500)
    kiln_start_time = forms.DateTimeField(required=True)
    kiln_finish_time = forms.DateTimeField(required=True)