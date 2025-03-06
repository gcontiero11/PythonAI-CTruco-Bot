from django.http import JsonResponse
from bot.game_model.card_to_play import CardToPlay
from bot.game_model.interfaces import BotServiceProvider
from bot.game_model.game_intel import GameIntel
from bot.django_remote_bot import DjangoRemoteBot;
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class BotViews(viewsets.ViewSet, BotServiceProvider):

  def __init__(self):
    self.bot_instance = DjangoRemoteBot()

  @method_decorator(csrf_exempt)
  @action(detail=False, methods=['post'], url_path='get_mao_de_onze_response')
  def get_mao_de_onze_response(self, request: Request):
    if not isinstance(request, Request): 
      request = Request(request, parsers=[JSONParser()]) 

    intel: GameIntel = GameIntel.from_dict(request.data)
    res = self.bot_instance.get_mao_de_onze_response(intel)
    
    print(res)
    return JsonResponse({"answer": res})

  @method_decorator(csrf_exempt)
  @action(detail=False, methods=['post'], url_path='decide_if_raises')   
  def decide_if_raises(self,request: Request):
    if not isinstance(request, Request): 
      request = Request(request, parsers=[JSONParser()]) 

    intel: GameIntel = GameIntel.from_dict(request.data)
    res = self.bot_instance.decide_if_raises(intel)

    return JsonResponse({"answer": res})
  
  @method_decorator(csrf_exempt)
  @action(detail=False, methods=['post'], url_path='choose_card')
  def choose_card(self,request: Request):

    if not isinstance(request, Request): 
      request = Request(request, parsers=[JSONParser()]) 

    intel: GameIntel = GameIntel.from_dict(request.data)
    res: CardToPlay = self.bot_instance.choose_card(intel)

    if res is None:
      return Response({"answer": "None"}, status=400)
    
    return JsonResponse(
      {"card_to_play":
       {"content": 
        {
          "rank": res.content.rank,
          "suit": res.content.suit
        },
      "discard": res.discard
      }
    })
  
  @method_decorator(csrf_exempt)
  @action(detail=False, methods=['post'], url_path='get_raise_response')
  def get_raise_response(self,request: Request):
    if not isinstance(request, Request): 
      request = Request(request, parsers=[JSONParser()]) 

    intel: GameIntel = GameIntel.from_dict(request.data)
    res: int = self.bot_instance.get_raise_response(intel)

    return JsonResponse({"answer": res}) 

  @method_decorator(csrf_exempt)
  @action(detail=False, methods=['get'], url_path='get_name')
  def get_name(self,request: Request):

    name = self.bot_instance.get_name()
    return name 