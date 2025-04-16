from django.http import JsonResponse
from bot.game_model.card_to_play import CardToPlay
from bot.game_model.interfaces import BotServiceProvider
from bot.game_model.game_intel import GameIntel
from bot.django_remote_bot import DjangoRemoteBot
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from bot.serializers.serializer import GameIntelSerializer
from bot.models import GameIntelModel

class BotViews(viewsets.ViewSet, BotServiceProvider):
    renderer_classes = [JSONRenderer]

    def __init__(self):
        self.bot_instance = DjangoRemoteBot()

    def _save_game_state(self, game_intel: GameIntel, decision_type: str, result: any):
        """Helper method to save game state"""
        model = GameIntelModel.from_game_intel(
            game_intel, 
            decision_type=decision_type,
            decision_result=result
        )
        model.save()

    @method_decorator(csrf_exempt)
    @action(detail=False, methods=['post'], url_path='get_mao_de_onze_response')
    def get_mao_de_onze_response(self, request: Request):
        if not isinstance(request, Request): 
            request = Request(request, parsers=[JSONParser()]) 

        serializer = GameIntelSerializer(data=request.data)
        if serializer.is_valid():
            game_intel = serializer.save()
            res: bool = self.bot_instance.get_mao_de_onze_response(game_intel)
            self._save_game_state(game_intel, "mao_de_onze", res)
            return JsonResponse(res, safe=False)
        return JsonResponse(serializer.errors, status=400)

    @method_decorator(csrf_exempt)
    @action(detail=False, methods=['post'], url_path='decide_if_raises')   
    def decide_if_raises(self,request: Request):
        if not isinstance(request, Request): 
            request = Request(request, parsers=[JSONParser()]) 
        
        print(request.data)
        serializer = GameIntelSerializer(data=request.data)
        if serializer.is_valid():
            game_intel = serializer.save()
            res = self.bot_instance.decide_if_raises(game_intel)
            self._save_game_state(game_intel, "decide_if_raises", res)
            return JsonResponse(res, safe=False)
        return JsonResponse(serializer.errors, status=400)
  
    @method_decorator(csrf_exempt)
    @action(detail=False, methods=['post'], url_path='choose_card')
    def choose_card(self,request: Request):
        if not isinstance(request, Request): 
            request = Request(request, parsers=[JSONParser()]) 

        serializer = GameIntelSerializer(data=request.data)
        if serializer.is_valid():
            game_intel = serializer.save()
            res: CardToPlay = self.bot_instance.choose_card(game_intel)
            
            if res is None:
                return JsonResponse(None, safe=False)
            
            self._save_game_state(game_intel, "choose_card", res.to_dict())
            return JsonResponse(res.to_dict())
        
        return JsonResponse(serializer.errors, status=400)
  
    @method_decorator(csrf_exempt)
    @action(detail=False, methods=['post'], url_path='get_raise_response')
    def get_raise_response(self,request: Request):
        if not isinstance(request, Request): 
            request = Request(request, parsers=[JSONParser()]) 

        serializer = GameIntelSerializer(data=request.data)
        if serializer.is_valid():
            game_intel = serializer.save()
            res: int = self.bot_instance.get_raise_response(game_intel)
            self._save_game_state(game_intel, "get_raise_response", res)
            return JsonResponse(res, safe=False)
        return JsonResponse(serializer.errors, status=400)

    @method_decorator(csrf_exempt)
    @action(detail=False, methods=['get'], url_path='get_name')
    def get_name(self, request: Request):
        name = self.bot_instance.get_name()
        return JsonResponse(name, safe=False)