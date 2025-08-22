from django.urls import path
from . import views

app_name = 'flights'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_flight, name='create'),
    path('list/', views.list_flights, name='list'),
    path('stats/', views.flight_stats, name='stats'),
]
