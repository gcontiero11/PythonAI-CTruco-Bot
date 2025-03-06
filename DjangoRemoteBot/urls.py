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

bot_views = BotViews()

urlpatterns = [
    path('admin', admin.site.urls),
    path('mao-de-onze', bot_views.get_mao_de_onze_response),
    path('name', bot_views.get_name),
    path('decide-if-raises', bot_views.decide_if_raises),	
    path('choose-card', bot_views.choose_card),
    path('raise-response', bot_views.get_raise_response),
]
