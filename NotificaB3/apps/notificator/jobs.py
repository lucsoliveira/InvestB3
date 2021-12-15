import http.client
import json

from django.conf import settings
from django.core.mail import send_mail

# import do model Alert
from alert.models import Alert
from django.contrib.auth.models import User

scheduler = settings.SCHEDULER


def notificator(*args):

    print(args[0])

    if args[0] != '':

        stock = args[0].code
        user_id = args[0].user_id
        higher_limit = args[0].higher_limit
        lower_limit = args[0].lower_limit
        sync = args[0].sync
        last_notification = args[0].last_notification

        print('--> stock: ' + stock + '| user_id:' + str(user_id) +
              ' higher: ' + str(higher_limit) + ' lower: ' + str(lower_limit) + ' \n')

        # get actual price
        actual_price = get_stock_actual_price(stock)

        # 0 to sell - 1 to buy
        if actual_price <= lower_limit:
            send_email(user_id, stock, actual_price, lower_limit, 1)

        if actual_price >= higher_limit:
            send_email(user_id, stock, actual_price, higher_limit, 0)

# function send email


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
            'Olá, ' + user.first_name + '! \nEssa é uma mensagem de aviso para venda da ação: ' +
            str(code_stock) + '. \nO Valor atual dela está em: (BRL) ' + str(actual_value_stock) +
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
