from django.urls import path
from . import views

app_name = 'alert'

urlpatterns = [
    path('', views.index, name='index'),
    path('remove/', views.remove, name='remove'),
    path('add/', views.add, name='add'),
    path('update/', views.update, name='update'),
]
