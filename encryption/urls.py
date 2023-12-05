from django.urls import path
from . import views
urlpatterns = [
path('encryption',views.encryption, name='encryption' ),
path('result',views.result, name='result' ),
]