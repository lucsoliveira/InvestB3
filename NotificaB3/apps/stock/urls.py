from django.urls import path
from . import views

app_name = 'stock'

urlpatterns = [
    path('', views.singleStock, name='single_stock'),
    #path('<str:code>/', views.singleStock, name='single_stock'),
]
