import django_tables2 as tables

from .models import Inspection


class InspectionTable(tables.Table):
    class Meta:
        model = Inspection
        template_name = 'includes/mytables.html'
        exclude = ('id', )
        attrs = {'class': 'table table-hover align-middle'}
