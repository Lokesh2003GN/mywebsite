from django.urls import path
from . import views
urlpatterns = [
path('rock_paper_scissor',views.rock_paper_scissor, name='rock_paper_scissor' ),
path('change_image',views.change_image, name='change_image' ),
]