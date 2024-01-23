from django.urls import path
from . import views

app_name = 'weather_app'

urlpatterns = [
    path('', views.confirm, name='confirm'),
]