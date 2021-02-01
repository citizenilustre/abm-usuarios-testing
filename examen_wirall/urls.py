"""examen_wirall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.urls import include
from tarjetas.views import abm_tarjetas
from personas.views import abm_personas

url_tarjetas = [
    path('abm_tarjetas', abm_tarjetas, name='abm_tarjetas'),
]

url_personas = [
    path('abm_personas', abm_personas, name='abm_personas'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tarjetas/', include(url_tarjetas)),
    path('personas/', include(url_personas)),
    path('', abm_personas, name='abm_personas')
]
