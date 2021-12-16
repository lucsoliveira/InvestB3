from collections import namedtuple
from django.conf import settings
from alert.models import Alert
from .jobs import notificator

from apscheduler.triggers.combining import AndTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger

scheduler = settings.SCHEDULER


def start():

    print("--> Inicializando o notificador...")

    # verificação inicial, se há alertas no banco e não no scheduler, criar estes scheduler's com mesmo uid
    alerts = Alert.objects.filter().values()
    print('Quantidade de alertas: ' + str(len(alerts)))
    if len(alerts) > 0:

        print('Há alertas no banco que ainda não foram setados no scheduler.')
        print('Setando jobs no scheduler...')

        for alert in alerts:

            # convert alert dictionary into an object in python
            a = namedtuple("alert", alert.keys())(*alert.values())

            scheduler.add_job(notificator, 'interval', id=alert['uid_scheduler'],
                              minutes=alert['interval_notify'], args=[a])

        print('Jobs setados no scheduler com sucesso.')
        print('All jobs: ', scheduler.get_jobs())
        scheduler.start()

    else:

        scheduler.start()

    print("<-- Notificador inicializado.")
