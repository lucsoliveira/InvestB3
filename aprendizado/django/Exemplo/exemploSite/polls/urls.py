from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # para acessar /polls/5
    path('<int:question_id>/', views.detail, name='detail'),
    # para acessar /polls/5/results
    path('<int:question_id>/results', views.results, name='results'),
    # para acessar /polls/5/vote
    path('<int:question_id>/vote', views.vote, name='vote'),
]
