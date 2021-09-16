from django.http.response import Http404, HttpResponseServerError
from django.shortcuts import redirect, render
from .models import Record
from .tables import RecordTable
from .forms import (
    RecordsFilterForm, MoistureContentRecordCreateForm, 
    SizeCheckRecordCreateForm, KilnTimeRecordCreateForm
)
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages


@login_required
def record_list(request):
    table = RecordTable(Record.objects.all())

    return render(request, "records/records.html", {
        "table": table,
        "filter_form": RecordsFilterForm()
    })

@login_required
def record_filter_ajax(request):
    record_type = request.GET.get('record_type', None)
    record_pass = request.GET.get('record_pass', None)
    query = Record.objects.all()

    if record_type:
        query = query.filter(record_type = record_type)

    if record_pass:
        query = query.filter(record_pass = True if record_pass == 'True' else False)

    return render(request, "records/components/records_table.html", {
        "table": RecordTable(query)
    })

@login_required
def record_create(request):
    record_type = request.GET.get('record_type', None)
    if request.method == 'GET':
        return render(request, "records/create.html")
    elif request.method == 'POST' and record_type:
        form = None
        if record_type == Record.RecordType.MOISTURE_CONTENT:
            form = MoistureContentRecordCreateForm(request.POST)
        elif record_type == Record.RecordType.SIZE_CHECK:
            form = SizeCheckRecordCreateForm(request.POST)
        elif record_type == Record.RecordType.KILN_TIME:
            form = KilnTimeRecordCreateForm(request.POST)
        else:
            messages.error(request, 'Invalid Record Type', extra_tags="record_type")

        if form and form.is_valid():
            record = Record(record_type=record_type, **form.cleaned_data)
            record.save()
            messages.success(request, 'Successfully Created!')
    else:
        messages.error(request, 'Invalid Request')

    return redirect("/records/")

@login_required
def record_create_form(request):
    record_type = request.GET.get('record_type', None)
    return render(request, "records/components/create_form.html", {
        "record_type": record_type,
        "moisture_form": MoistureContentRecordCreateForm(),
        "size_form": SizeCheckRecordCreateForm(),
        "kiln_form": KilnTimeRecordCreateForm()
    })

@login_required
def record_edit(request, pk=None):
    record = Record.objects.filter(pk=pk).first()
    if not record:
        return Http404()

    if request.method == 'POST':
        form = None
        if record.record_type == "MOISTURE_CONTENT":
            form = MoistureContentRecordCreateForm(request.POST)
        elif record.record_type == "SIZE_CHECK":
            form = SizeCheckRecordCreateForm(request.POST)
        elif record.record_type == "KILN_TIME":
            form = KilnTimeRecordCreateForm(request.POST)

        if form and form.is_valid():
            for key in form.cleaned_data:
                setattr(record, key, form.cleaned_data[key])
            record.save()
            messages.success(request, 'Successfully Updated!')
            return redirect('/records/')
    else:
        form = None
        if record.record_type == "MOISTURE_CONTENT":
            form = MoistureContentRecordCreateForm(record.__dict__)
        elif record.record_type == "SIZE_CHECK":
            form = SizeCheckRecordCreateForm(record.__dict__)
        elif record.record_type == "KILN_TIME":
            form = KilnTimeRecordCreateForm(record.__dict__)

        if form and form.is_valid():
            return render(request, "records/edit.html", {
                "data": record,
                "form": form
            })

    return HttpResponseServerError()

@login_required
def record_delete(request, pk=None):
    record = Record.objects.filter(pk=pk).first()
    if not record:
        return Http404()
    record.delete()
    messages.success(request, 'Successfully Deleted!')
    return redirect('/records/')