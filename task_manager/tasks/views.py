from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from django_tables2 import SingleTableView

from .forms import InspectionForm
from .models import Inspection
from .tables import InspectionTable
from task_manager.settings import PAGINATE_BY  # type: ignore


User = get_user_model()


def index(request):
    return render(request, 'index.html', {})


class InspectionListView(SingleTableView):
    model = Inspection
    table_class = InspectionTable
    template_name = 'inspections.html'
    paginate_by = PAGINATE_BY

    def get_table_data(self):
        return Inspection.objects.filter(user=self.request.user)


@login_required
def new_inspection(request):
    form = InspectionForm(request.POST or None)
    if form.is_valid():
        inspection = form.save(commit=False)
        inspection.user = request.user
        inspection.save()
        return redirect('tasks:inspections')
    return render(
        request, 'new_task.html',
        {'form': form, 'is_new': True}
    )


@login_required
def edit_inspection(request, insp_id):
    inspection = get_object_or_404(Inspection, id=insp_id)
    form = InspectionForm(request.POST or None, instance=inspection)
    if form.is_valid():
        inspection = form.save(commit=False)
        inspection.user = request.user
        inspection.save()
        return redirect('tasks:inspections')
    return render(
        request, 'new_task.html',
        {'form': form, 'insp_id': inspection.id, 'is_new': False}
    )


@login_required
def del_inspection(request, insp_id):
    inspection = get_object_or_404(Inspection, id=insp_id)
    if inspection.user == request.user:
        inspection.delete()
    return redirect('tasks:inspections')
