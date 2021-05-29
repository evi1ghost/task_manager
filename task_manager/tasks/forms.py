from django.forms import ModelForm

from .models import Inspection


class InspectionForm(ModelForm):
    class Meta:
        model = Inspection
        exclude = ['id', 'user']
        error_messages = {
            'inspection_type': {
                'required': 'Укажите тип провеки'
            },
            'inspector': {
                'required': 'Укажите проверяющий орган'
            },
            'region': {
                'required': 'Укажите регион'
            },
            'description': {
                'required': 'Добавьте описание'
            },
            'result': {
                'required': 'Укажите статус/результат проверки'
            },
        }
