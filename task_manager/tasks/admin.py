from django.contrib import admin

from .models import Claim, Inspection, Region, Trial


@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'user', 'date', 'inspection_type', 'inspector', 'region',
        'adress', 'description', 'comment', 'event', 'result',
    )
    search_fields = ('adress',)
    list_filter = ('date', 'region', 'inspection_type', 'user',)
    empty_value_display = '-пусто-'


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'region',)
    empty_values_display = '-пусто-'


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'user', 'date', 'type', 'counterparty', 'region',
        'adress', 'description', 'comment', 'result',
    )
    search_fields = ('counterparty', 'adress',)
    list_filter = ('region', 'type', 'user',)


@admin.register(Trial)
class TrialAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'user', 'initial_date', 'court', 'case_number', 'plaintiff',
        'defendant', 'amount', 'subject', 'comment', 'posible_result',
        'result'
    )
