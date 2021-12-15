import http.client
import json

from django.shortcuts import render
from alert.models import Alert
from django.http import HttpResponse

# Create your views here.
# conexão com a API
conn = http.client.HTTPSConnection("yh-finance.p.rapidapi.com")
headers = {
    'x-rapidapi-host': "yh-finance.p.rapidapi.com",
    'x-rapidapi-key': "9efcbecc6dmsh53d821d294f159dp1e0906jsn3e1bae122453"
}


def index(request):
    """View da pagina stock"""
    # TODO: Se vazio, redirecionar para a tela market
    return render(request, 'stock.html')


def singleStock(request):
    """View of stock page"""

    code = request.GET.get('q')

    # get data from API

    context = {
        'code': code,
    }

    # verify if this stock is alert
    try:
        context['alert'] = Alert.objects.get(
            user_id=request.user.id, code=code)

    except Alert.DoesNotExist:
        pass

    return render(request, 'stock/index.html', context=context)
