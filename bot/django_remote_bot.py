from bot.game_model.game_intel import GameIntel
from bot.game_model.card_to_play import CardToPlay
from bot.game_model.interfaces import BotServiceProvider

class DjangoRemoteBot(BotServiceProvider):
    def __init__(self):
        pass

    def get_mao_de_onze_response(self, intel: GameIntel) -> bool:
        return False

    def decide_if_raises(self, intel: GameIntel) -> bool:
        return True

    def choose_card(self, intel: GameIntel) -> CardToPlay:
        return CardToPlay(intel.cards[0], False)

    def get_raise_response(self, intel: GameIntel) -> int:
        return 0
