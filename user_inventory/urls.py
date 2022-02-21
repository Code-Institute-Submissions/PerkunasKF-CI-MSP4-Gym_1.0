from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_inventory, name='user_inventory'),
    path('order_history_unique/<order_number>', views.order_history_unique, name='order_history_unique'),
]