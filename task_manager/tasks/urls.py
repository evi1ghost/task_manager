from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views


app_name = 'tasks'


urlpatterns = [
    path('', views.index, name='index'),
    path(
        'inspections/', login_required(views.InspectionListView.as_view()),
        name='inspections'
    ),
    path('new_inspection/', views.new_inspection, name='new_inspection'),
    path(
        'edit_inspection/<int:insp_id>/',
        views.edit_inspection, name='edit_inspection'
    )
]
