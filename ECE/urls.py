from django.urls import path
from . import views

urlpatterns = [
path('resistor',views.resistor, name='resistor' ),
path('resistor_result',views.resistor_result,name='resistor_result'),
]