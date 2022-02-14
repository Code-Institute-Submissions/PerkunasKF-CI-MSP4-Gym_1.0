from django.urls import path
from . import views

urlpatterns = [
    path('unique_buy/<item_id>', views.unique_buy, name='unique_buy'),
]
