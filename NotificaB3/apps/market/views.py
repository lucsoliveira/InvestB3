from django.shortcuts import render


def index(request):
    """View da pagina mercado"""
    context = {
        'title_site': 'Mercado de Ações | NotificaB3 - Desafio INOA'
    }
    return render(request, 'market/index.html', context=context)
