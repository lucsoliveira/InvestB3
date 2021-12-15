from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler


from django.conf import settings

scheduler = settings.SCHEDULER


def start():

    print("--> Inicializando o notificador...")

    # verificação inicial, se há alertas no banco e não no scheduler, criar estes scheduler's com mesmo uid
    scheduler.start()

    print("<-- Notificador inicializado.")
