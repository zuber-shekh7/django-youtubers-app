from django.urls import path

from . import views

app_name = 'teams'

urlpatterns = [
    path('', views.list_team_members, name='list-team-members'),
]
