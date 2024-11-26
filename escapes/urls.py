from django.urls import path

from . import views

app_name = 'escapes'

urlpatterns = [
    path('', views.escapes_home, name='index'),
]