from django.contrib.auth import get_user_model
# from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django_tables2 import SingleTableView

from .models import Inspection
from .tables import InspectionTable


User = get_user_model()


def index(request):
    return render(request, 'index.html', {})


class InspectionListView(SingleTableView):
    model = Inspection
    table_class = InspectionTable
    template_name = 'inspections.html'
    paginate_by = 10

    def get_table_data(self):
        return Inspection.objects.filter(user=self.request.user)
