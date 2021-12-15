import http.client
import json

from django.shortcuts import render
from alert.models import Alert
from django.http import JsonResponse

from django.conf import settings

# Yahoo Finances API Key
isSafe = False

# stock - single - get


def getStock(request):

    code = request.GET.get('code')

    if request.user.id:

        # get data from API
        conn = http.client.HTTPSConnection(settings.URL_SERVER_API)
        conn.request("GET", "/auto-complete?q=" +
                     code + "&region=BR", headers=settings.HEADERS_API)
        res = conn.getresponse()
        data = res.read()
        conn.close()

        return JsonResponse(json.loads(data.decode("utf-8")), status=201, safe=isSafe)

    else:
        # só é possivel obter estes dados se o usuário estiver logado
        return JsonResponse({'error': 'Usuário não logado.'}, status=404, safe=isSafe)


# stock - single - quotes - get
def getStockQuotes(request):

    code = request.GET.get('code')

    if request.user.id:

        # get data from API

        conn = http.client.HTTPSConnection(settings.URL_SERVER_API)
        conn.request("GET", "/market/v2/get-quotes?region=BR&symbols=" +
                     code + ".SA", headers=settings.HEADERS_API)
        res = conn.getresponse()
        data = res.read()

        conn.close()
        return JsonResponse(json.loads(data.decode("utf-8")), status=201, safe=isSafe)

    else:
        # só é possivel obter estes dados se o usuário estiver logado
        return JsonResponse({'error': 'Usuário não logado.'}, status=404, safe=isSafe)


# stock - b3 - all - get
def getAllStocks(request):

    if request.user.id:
        # get data from API
        conn = http.client.HTTPSConnection("api-cotacao-b3.labdo.it")
        conn.request("GET", "/api/empresa")
        res = conn.getresponse()
        data = res.read()

        conn.close()
        return JsonResponse(json.loads(data.decode("utf-8")), status=201, safe=isSafe)

    else:
        # só é possivel obter estes dados se o usuário estiver logado
        return JsonResponse({'error': 'Usuário não logado.'}, status=404, safe=isSafe)


# stock - news - get


def getStockNews(request):

    code = request.GET.get('code')

    if request.user.id:

        if (code is None):

            # só é possivel obter estes dados se o usuário estiver logado
            return JsonResponse({'error': 'Não foi possível obter os dados.'}, status=404, safe=isSafe)

        else:

            # get data from API

            conn = http.client.HTTPSConnection(settings.URL_SERVER_API)
            conn.request("GET", "/auto-complete?q=" +
                         code + "&region=BR", headers=settings.HEADERS_API)
            res = conn.getresponse()
            data = res.read()
            conn.close()

            return JsonResponse({"code": code, 'news': json.loads(data.decode("utf-8"))['news']}, status=201, safe=isSafe)

    else:
        # só é possivel obter estes dados se o usuário estiver logado
        return JsonResponse({'error': 'Não foi possível obter os dados.'}, status=404, safe=isSafe)


# stock - single - quotes - price


def getStockQuotesPrice(request):

    code = request.GET.get('code')

    if request.user.id:

        if (code is None):

            # só é possivel obter estes dados se o usuário estiver logado
            return JsonResponse({'error': 'Não foi possível obter os dados.'}, status=404, safe=isSafe)

        else:

            # get data from API

            conn = http.client.HTTPSConnection(settings.URL_SERVER_API)
            conn.request("GET", "/market/v2/get-quotes?region=BR&symbols=" +
                         code + ".SA", headers=settings.HEADERS_API)
            res = conn.getresponse()
            data = res.read()
            conn.close()

            return JsonResponse({"code": code, 'price': json.loads(data.decode("utf-8"))['quoteResponse']['result'][0]['regularMarketPrice']}, status=201, safe=isSafe)

    else:
        # só é possivel obter estes dados se o usuário estiver logado
        return JsonResponse({'error': 'Não foi possível obter os dados.'}, status=404, safe=isSafe)


# stock - summary - quotes - get
def getStockSummaryAndQuotes(request):

    code = request.GET.get('code')

    if request.user.id:

        if (code is None):

            # só é possivel obter estes dados se o usuário estiver logado
            return JsonResponse({'error': 'Não foi possível obter os dados.'}, status=404, safe=isSafe)

        else:

            # get summary stock
            conn = http.client.HTTPSConnection(settings.URL_SERVER_API)
            conn.request("GET", "/stock/v2/get-summary?symbol=" +
                         code + "&region=BR", headers=settings.HEADERS_API)
            resSummary = conn.getresponse()
            dataSummary = resSummary.read()
            conn.close()

            # get stock quotes
            conn = http.client.HTTPSConnection(settings.URL_SERVER_API)
            conn.request("GET", "/market/v2/get-quotes?region=BR&symbols=" +
                         code + ".SA", headers=settings.HEADERS_API)
            resQuotes = conn.getresponse()
            dataQuotes = resQuotes.read()
            conn.close()

            print("dataSummary", dataSummary)

            return JsonResponse({"summary": json.loads(dataSummary.decode("utf-8")), "quotes": json.loads(dataQuotes.decode("utf-8"))['quoteResponse']['result']}, status=201, safe=isSafe)

    else:
        # só é possivel obter estes dados se o usuário estiver logado
        return JsonResponse({'error': 'Não foi possível obter os dados.'}, status=404, safe=isSafe)


# alerts - user - all - get


def getAllUserAlerts(request):

    id_user = request.GET.get('idUser')

    if request.user.id:

        if id_user is None:

            # só é possivel obter estes dados se o usuário estiver logado
            return JsonResponse({'error': 'Parâmetros faltantes para requisição.'}, status=404, safe=isSafe)

        else:

            # verify if logged user is the user id
            if request.user.id == int(id_user):

                alerts = Alert.objects.filter(
                    user=request.user.id).values()
                listAlerts = list(alerts)

                # add the stock actual price in the values
                for i in listAlerts:

                    # get from API getStockQuotesPrice

                    conn = http.client.HTTPSConnection(settings.URL_SERVER_API)
                    conn.request("GET", "/market/v2/get-quotes?region=BR&symbols=" +
                                 i['code'] + ".SA", headers=settings.HEADERS_API)
                    res = conn.getresponse()
                    data = res.read()
                    conn.close()
                    i["longname"] = json.loads(data.decode(
                        "utf-8"))['quoteResponse']['result'][0]['longName']
                    i["actualPrice"] = json.loads(data.decode(
                        "utf-8"))['quoteResponse']['result'][0]['regularMarketPrice']

                return JsonResponse({"alerts": listAlerts}, status=201, safe=isSafe)

            else:
                return JsonResponse({'error': 'Pedido divergente de usuário logado'}, status=404, safe=isSafe)

    else:
        # só é possivel obter estes dados se o usuário estiver logado
        return JsonResponse({'error': 'Não há usuário logado.'}, status=404, safe=isSafe)

# alerts - users - all - get


def getAllAlerts(request):

    # verify if logged user is the user id

    alerts = Alert.objects.filter().values()
    listAlerts = list(alerts)

    key = request.GET.get('key')

    if key == 'yourkeymasterhere':

        for i in listAlerts:

            # get from API getStockQuotesPrice
            conn = http.client.HTTPSConnection(settings.URL_SERVER_API)
            conn.request("GET", "/market/v2/get-quotes?region=BR&symbols=" +
                         i['code'] + ".SA", headers=settings.HEADERS_API)
            res = conn.getresponse()
            data = res.read()
            conn.close()

            i["longname"] = json.loads(data.decode(
                "utf-8"))['quoteResponse']['result'][0]['longName']
            i["actual_price"] = json.loads(data.decode(
                "utf-8"))['quoteResponse']['result'][0]['regularMarketPrice']

        return JsonResponse({"alerts": listAlerts}, status=201, safe=isSafe)

    else:

        return JsonResponse({'error': 'Key wrong.'}, status=404, safe=isSafe)
