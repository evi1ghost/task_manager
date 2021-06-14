from django.contrib.auth import get_user_model

import django_filters

from .models import Inspection, Region


User = get_user_model()


class InspectionFilter(django_filters.FilterSet):
    user = django_filters.ModelChoiceFilter(
        queryset=User.objects.all()
    )
    date = django_filters.DateFromToRangeFilter(label='Период')
    inspection_type = django_filters.ChoiceFilter(
        choices=Inspection.INSPECTION_TYPE
    )
    inspector = django_filters.CharFilter(
        label='Проверяющий орган', lookup_expr='icontains'
    )
    region = django_filters.ModelChoiceFilter(
        queryset=Region.objects.all()
    )
    adress = django_filters.CharFilter(
        label='Адрес', lookup_expr='icontains'
    )
    description = django_filters.CharFilter(
        label='Описание', lookup_expr='icontains'
    )
    comment = django_filters.CharFilter(
        label='Комментарий', lookup_expr='icontains'
    )
    event = django_filters.CharFilter(
        label='События в рамках проверки', lookup_expr='icontains'
    )
    result = django_filters.CharFilter(
        label='Результат/статус', lookup_expr='icontains'
    )

    class Meta:
        model = Inspection
        exclude = ['id', ]


class PersonalInspectionFilter(InspectionFilter):
    class Meta:
        model = Inspection
        exclude = ['id', 'user']
