"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # sistema de autenticação
    path('accounts/', include('django.contrib.auth.urls')),
    # api REST
    path('api/', include('api.urls', namespace='api')),
    # favorites, pagina single de uma ação
    path('alert/', include('alert.urls', namespace='alert')),
    path('', RedirectView.as_view(url='alert/')),
    # stocks, pagina single de uma ação
    path('stock/', include('stock.urls', namespace='stock')),
    # mercado de ações com listagem para adicionar aos favoritos
    path('market/', include('market.urls')),

]
