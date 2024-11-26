from django.urls import path

from . import views

app_name = 'escapes_api'

urlpatterns = [
    path('', views.escapes_api_home, name='api_index'),
]