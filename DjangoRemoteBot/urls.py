"""
URL configuration for DjangoRemoteBot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from bot.views import BotViews

urlpatterns = [
    path('admin', admin.site.urls),
    path('mao-de-onze', BotViews.as_view({'post': 'get_mao_de_onze_response'})),
    path('name', BotViews.as_view({'get': 'get_name'})),
    path('if-raises', BotViews.as_view({'post': 'decide_if_raises'})),
    path('choose-card', BotViews.as_view({'post': 'choose_card'})),
    path('raise-response', BotViews.as_view({'post': 'get_raise_response'})),
]
