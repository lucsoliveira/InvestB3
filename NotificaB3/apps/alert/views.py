import json

from typing import Reversible
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .forms import RemoveAlertForm, AddAlertForm, UpdateAlertForm

from .models import Alert, User


def index(request):
    """View da pagina alertas"""
    context = {
        'user': request.user,
    }

    return render(request, 'alert/index.html')


def add(request):

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        form = AddAlertForm(request.POST)

        if form.is_valid():
            code = form.cleaned_data['code']
            interval_notify = form.cleaned_data['interval_notify']
            higher_limit = form.cleaned_data['higher_limit']
            lower_limit = form.cleaned_data['lower_limit']

            if request.user:

                f = Alert(user_id=request.user.id, code=code,
                          interval_notify=interval_notify, higher_limit=higher_limit, lower_limit=lower_limit, sync=0)
                f.save()

                return HttpResponseRedirect('/')

            else:
                return HttpResponseRedirect('/errorUser')
        else:

            return HttpResponseRedirect('/errorForm')

    return render(request, 'index.html')


def update(request):

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        form = UpdateAlertForm(request.POST)

        if form.is_valid():

            id_alert = form.cleaned_data['id_alert']
            code = form.cleaned_data['code']
            interval_notify = form.cleaned_data['interval_notify']
            higher_limit = form.cleaned_data['higher_limit']
            lower_limit = form.cleaned_data['lower_limit']

            if request.user:

                f = Alert.objects.get(
                    user_id=request.user.id, id=id_alert)

                if f:
                    f.code = code
                    f.interval_notify = interval_notify
                    f.higher_limit = higher_limit
                    f.lower_limit = lower_limit

                    f.save()

                    return HttpResponseRedirect('/')

            else:
                return HttpResponseRedirect('/errorUser')
        else:

            return HttpResponseRedirect('/errorForm')

    return render(request, 'index.html')


def remove(request):

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        form = RemoveAlertForm(request.POST)

        if form.is_valid():
            # redirect to a new URL:
            id_alert = form.cleaned_data['id_alert']

            if request.user:

                Alert.objects.filter(
                    user=request.user.id, id=id_alert).delete()
                return HttpResponseRedirect('/')

            else:
                return HttpResponseRedirect('/')

    return render(request, 'index.html')
