import django_tables2 as tables

from .models import Inspection


class InspectionTable(tables.Table):
    edit = tables.TemplateColumn(
        template_code='<i class="far fa-edit"></i>',
        linkify=(
            'tasks:edit_inspection',
            {'insp_id': tables.A('id')}
        ),
        orderable=False,
        empty_values=(),
        verbose_name=' '
    )

    class Meta:
        model = Inspection
        template_name = 'includes/mytables.html'
        exclude = ('id', )
        attrs = {'class': 'table table-hover align-middle'}
