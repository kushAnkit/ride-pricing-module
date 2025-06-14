from django.urls import path
from .views import calculate_fare
from .views import config_form_view

urlpatterns = [
    path('calculate-fare/', calculate_fare, name='calculate_fare'),
]