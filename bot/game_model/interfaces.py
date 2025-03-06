from abc import ABC, abstractmethod
from django.http import JsonResponse
from bot.game_model.card_to_play import CardToPlay
from bot.game_model.game_intel import GameIntel

class BotServiceProvider(ABC):
  @abstractmethod
  def get_mao_de_onze_response(self,intel: GameIntel) -> bool:
    raise NotImplementedError
  
  @abstractmethod
  def decide_if_raises(self,intel: GameIntel) -> bool:
    raise NotImplementedError
  
  @abstractmethod
  def choose_card(self,intel: GameIntel) -> CardToPlay:
    raise NotImplementedError
  
  @abstractmethod
  def get_raise_response(self,intel: GameIntel) -> int:
    raise NotImplementedError
  
  def get_name(self) -> str:
    return JsonResponse({"name": self.__class__.__name__})