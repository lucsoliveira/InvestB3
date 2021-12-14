from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    # Stock
    path('stock/get/', views.getStock, name='getStock'),
    path('stock/news/get/', views.getStockNews, name='getStockNews'),
    path('stock/quotes/get/', views.getStockQuotes, name='getStockQuotes'),
    path('stock/quotes/price/get/', views.getStockQuotesPrice,
         name='getStockQuotesPrice'),
    path('stock/summary/quotes/get/', views.getStockSummaryAndQuotes,
         name='getStockSummaryAndQuotes'),
    path('stock/b3/all/get/', views.getAllStocks, name='getAllStocks'),
    # Alert
    path('alert/all/get/', views.getAllUserAlerts,
         name='getAllUserAlerts'),
]
