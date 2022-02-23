from django.urls import path
from . import views


urlpatterns = [
    path('', views.comunity, name='comunity'),
    path('<username>', views.comunity, name='comunity'),
]
