from django.urls import path
from . import views

urlpatterns = [
path('numbers',views.numbers, name='numbers' ),
path('numbers_result',views.numbers_result, name='numbers_result' ),
path('tables',views.tables,name='tables'),
path('tables_result',views.tables_result,name='tables_result'),
path('factorial',views.factorial,name='factorial'),
path('factorial_result',views.factorial_result,name='factorial_result'),
path('decimal_binary_conversation',views.decimal_binary_conversation,name='decimal_binary_conversation'),
path('decimal_binary_conversation_result',views.decimal_binary_conversation_result,name='decimal_binary_conversation_result'),
    
]
