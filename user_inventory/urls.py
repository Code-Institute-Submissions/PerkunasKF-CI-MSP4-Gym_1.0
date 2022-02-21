from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_inventory, name='user_inventory'),
    # path('order_history/<order_number>', views.order_history, name='order_history'),
]