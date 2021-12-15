from django.http import request
from django.shortcuts import render


def index(request):
    """View da pagina mercado"""
    return render(request, 'market/index.html')
