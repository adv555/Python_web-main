from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns = [
    path('', views.index, name='index'),
    path('statistics/', views.statistics, name='statistics'),
]
