from django.urls import path

from . import views

app_name = 'youtubers'

urlpatterns = [
    path('', views.list_youtubers, name='list-youtubers'),
]
