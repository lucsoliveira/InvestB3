from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# models
from .models import Question

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("Você está procurando pela questão %s. " % question_id)


def results(request, question_id):
    response = "Você quer os resultados de %s. "
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Você está votando na questão %s. " % question_id)
