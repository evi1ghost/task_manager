from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views


app_name = 'tasks'


urlpatterns = [
    path('', views.index, name='index'),
    path('inspections/',
         login_required(views.PersonalInspectionListView.as_view()),
         name='inspections'),
    path('inspections/new/', views.new_inspection, name='new_inspection'),
    path('inspections/<int:insp_id>/edit/',
         views.edit_inspection, name='edit_inspection'),
    path('inspection/<int:insp_id>/delete',
         views.del_inspection, name='del_inspection'),
    path('inspections/all/',
         login_required(views.AllInspectionListView.as_view()),
         name='all_inspections')
]
