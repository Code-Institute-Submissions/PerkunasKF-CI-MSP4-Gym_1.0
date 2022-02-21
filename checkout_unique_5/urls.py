from django.urls import path
from . import views
# from .webhooks import webhook

urlpatterns = [
    # path('checkout_unique_form/<int:item_id>/', views.checkout_unique_form, name='checkout_unique_form'),
    path('checkout_unique/<int:item_id>/', views.checkout_unique, name='checkout_unique'),
    path('checkout_success_unique/<order_number>', views.checkout_success_unique, name='checkout_success_unique'),
    # path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    # path('wh/', webhook, name='webhook'),
]
