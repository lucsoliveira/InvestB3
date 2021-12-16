from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Alert
from .forms import RemoveAlertForm, AddAlertForm, UpdateAlertForm
from django.conf import settings
from notificator.jobs import notificator


def index(request):
    """View da pagina alertas"""
    context = {
        'title_site': 'Meus Alertas | NotificaB3 - Desafio INOA'
    }
    return render(request, 'alert/index.html', context=context)


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

                # create a job
                settings.SCHEDULER.add_job(
                    notificator, 'interval', minutes=interval_notify, args=[''])

                all_jobs = settings.SCHEDULER.get_jobs()

                last_job = all_jobs[len(all_jobs) - 1].id
                print('Job adicionado com sucesso!', all_jobs)

                a = Alert(uid_scheduler=last_job, user_id=request.user.id, code=code,
                          interval_notify=interval_notify, higher_limit=higher_limit, lower_limit=lower_limit, sync=0)
                a.save()

                # update the job with the parameters of alert
                all_jobs[len(all_jobs) - 1].modify(args=[a])

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

                a = Alert.objects.get(
                    user_id=request.user.id, id=id_alert)

                if a:

                    a.code = code
                    a.interval_notify = interval_notify
                    a.higher_limit = higher_limit
                    a.lower_limit = lower_limit

                    a.save()

                    # change the time os schedule job
                    settings.SCHEDULER.reschedule_job(
                        a.uid_scheduler, trigger='cron', minute='*/' + str(a.interval_notify))

                    settings.SCHEDULER.modify_job(a.uid_scheduler, args=[a])

                    # update the job with the parameters of alert

                    print('Job #' + str(a.uid_scheduler) +
                          ' atualizado com sucesso.')

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

                # retrive the alert
                a = Alert.objects.filter(
                    user=request.user.id, id=id_alert)

                # delete the job
                settings.SCHEDULER.remove_job(a[0].uid_scheduler)
                print('Job removido ' + a[0].uid_scheduler + ' com sucesso.')
                # delete de alert object
                a.delete()
                print('Alerta removido com sucesso.')

                # list all jobs in console
                print('All jobs: ', settings.SCHEDULER.get_jobs())
                return HttpResponseRedirect('/?msg=delete-sucess')

            else:
                return HttpResponseRedirect('/')

    return render(request, 'index.html')
