from django.urls import path
from . import views

urlpatterns = [
    path('', views.plans, name='plans'),
    path('<int:plan_id>/', views.plan_details, name='plan_details'),
]
