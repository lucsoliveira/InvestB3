import datetime
import http.client
import json

from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User

from alert.models import Alert

scheduler = settings.SCHEDULER
dt = datetime


def notificator(*args):

    # verify if the market is open
    week_days_market = settings.DAY_OF_WEEK_SCHEDULER
    hours_market = settings.HOUR_OPEN_CLOSE_MARKET_SCHEDULER

    week_day_now = dt.datetime.today().weekday()
    hour_now = dt.datetime.today().hour

    for i in week_days_market:

        if week_day_now == i and hours_market[0] <= hour_now <= hours_market[1]:

            if args[0] != '':

                idAlert = args[0].id
                stock = args[0].code
                user_id = args[0].user_id
                higher_limit = args[0].higher_limit
                lower_limit = args[0].lower_limit
                sync = args[0].sync
                last_notification = args[0].last_notification
                uid_scheduler = args[0].uid_scheduler

                print('--> stock: ' + stock + '| user_id:' + str(user_id) +
                      ' higher: ' + str(higher_limit) + ' lower: ' + str(lower_limit) + ' \n')

                # get actual price
                actual_price = get_stock_actual_price(stock)
                #actual_price = 12

                # 0 to sell - 1 to buy
                if actual_price <= lower_limit:

                    # verify the last notification
                    if verify_last_notify(last_notification) == 1:

                        change_last_notification(args[0])
                        send_email(user_id, stock,
                                   actual_price, lower_limit, 1)

                if actual_price >= higher_limit:

                    # verify the last notification
                    if verify_last_notify(last_notification) == 1:

                        change_last_notification(args[0])
                        send_email(user_id, stock, actual_price,
                                   higher_limit, 0)

# verify last notify


def verify_last_notify(last):

    last = dt.datetime.fromisoformat(str(last))
    actual = dt.datetime.today()

    hour_last = last.hour - 2
    hour_actual = actual.hour

    minutes_last = last.minute
    minutes_actual = actual.minute

    if hour_actual > hour_last:

        # change the last notify
        return 1

    else:

        diff_minutes = minutes_actual - minutes_last

        if diff_minutes >= settings.EMAIL_INTERVAL_SCHEDULER:

            # change the last notify
            return 1
        else:
            return 0


def change_last_notification(alert):

    a = Alert.objects.get(id=alert.id)
    a.last_notification = dt.datetime.today
    a.save()

    # change the last notification in the job
    settings.SCHEDULER.modify_job(alert.uid_scheduler, args=[a])

    print('Alerta e Job: ultima notificação atualizada com sucesso.')

    return 0


def send_email(*args):

    id_user = args[0]
    code_stock = args[1]
    actual_value_stock = args[2]
    limit_stock = args[3]
    type_email = args[4]  # 0 to sell - 1 to buy

    print('XXXXXX')
    print('Enviando email...')

    if type_email == 0:

        user = get_user(id_user)
        print('Tipo: Venda agora, valor maior')
        send_mail(
            '[NOTIFICAB3] Venda a ação: ' + str(code_stock),
            'Olá, ' + user.first_name + '!\nEssa é uma mensagem de aviso para venda da ação: ' +
            str(code_stock) + '.\nO Valor atual dela está em: (BRL) ' + str(actual_value_stock) +
            ' e seu limite para venda foi de: (BRL) ' +
            str(limit_stock) + ' .',
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False
        )

    else:
        user = get_user(id_user)
        print('Tipo: Compra agora, valor menor')
        send_mail(
            '[NOTIFICAB3] Compre a ação: ' + str(code_stock),
            'Olá, ' + user.first_name + '! \n Essa é uma mensagem de aviso para compra da ação: ' +
            str(code_stock) + '. \nO Valor atual dela está em: (BRL) ' + str(actual_value_stock) +
            ' e seu limite para compra foi de: (BRL) ' +
            str(limit_stock) + ' .',
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False
        )

    print('Email enviado com sucesso.')
    print('XXXXXX')


def get_stock_actual_price(code):

    conn = http.client.HTTPSConnection(settings.URL_SERVER_API)
    conn.request("GET", "/market/v2/get-quotes?region=BR&symbols=" +
                 code + ".SA", headers=settings.HEADERS_API)
    res = conn.getresponse()
    data = res.read()
    conn.close()

    actual_price = json.loads(data.decode(
        "utf-8"))['quoteResponse']['result'][0]['regularMarketPrice']

    print('--> Code: ' + code + '| Actual Price: ' + str(actual_price))

    return actual_price

# get user


def get_user(id):

    user = User.objects.get(pk=id)
    if user:
        return user
    else:
        return ''
