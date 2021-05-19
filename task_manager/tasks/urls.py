from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views


app_name = 'tasks'


urlpatterns = [
    path('', views.index, name='index'),
    # path(
    #     'inspections/', views.inspections, name='inspections'
    # ),
    path(
        'inspections/', login_required(views.InspectionListView.as_view()),
        name='inspections'
    )
]