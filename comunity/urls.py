from django.urls import path
from . import views


urlpatterns = [
    path('', views.comunity, name='comunity')
]
