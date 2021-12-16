import http.client
import json

from django.shortcuts import render
from alert.models import Alert


def index(request):
    """View da pagina stock"""
    # TODO: Se vazio, redirecionar para a tela market
    return render(request, 'stock.html')


def singleStock(request):
    """View of stock page"""

    code = request.GET.get('q')

    # get data from API

    if code:

        context = {
            'code': code,
            'title_site': code + '| NotificaB3 - Desafio INOA'
        }

        # verify if this stock is alert
        try:
            context['alert'] = Alert.objects.get(
                user_id=request.user.id, code=code)

        except Alert.DoesNotExist:
            pass

        return render(request, 'stock/index.html', context=context)

    else:

        context = {
            'title_site': 'Ação não encontrada | NotificaB3 - Desafio INOA'
        }
        return render(request, 'stock/index.html', context=context)
