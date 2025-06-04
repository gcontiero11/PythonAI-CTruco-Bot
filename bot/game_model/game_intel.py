from typing import List, Optional
from bot.game_model.truco_card import TrucoCard
# import numpy as np


class GameIntel:
    class RoundResult:
        WON = "WON"
        DREW = "DREW"
        LOST = "LOST"

    def __init__(self, cards: List['TrucoCard'], open_cards: List['TrucoCard'], vira: 'TrucoCard',
                 opponent_card: Optional['TrucoCard'], round_results: List[str], score: int, opponent_score: int,
                 hand_points: int):
        self.cards = cards
        self.open_cards = open_cards
        self.vira = vira
        self.opponent_card = opponent_card
        self.round_results = round_results
        self.score = score
        self.opponent_score = opponent_score
        self.hand_points = hand_points

    def get_cards(self) -> List['TrucoCard']:
        """
        Retorna as cartas que o jogador possui na mão.
        """
        return self.cards

    def get_open_cards(self) -> List['TrucoCard']:
        """
        Retorna as cartas abertas, incluindo a carta vira como o primeiro elemento.
        """
        return self.open_cards

    def get_vira(self) -> 'TrucoCard':
        """
        Retorna a carta vira da rodada.
        """
        return self.vira

    def get_opponent_card(self) -> Optional['TrucoCard']:
        """
        Retorna a carta jogada pelo oponente, ou None se o jogador for o primeiro a jogar.
        """
        return self.opponent_card

    def get_round_results(self) -> List[str]:
        """
        Retorna os resultados das rodadas até o momento.
        """
        return self.round_results

    def get_score(self) -> int:
        """
        Retorna a pontuação do jogador.
        """
        return self.score

    def get_opponent_score(self) -> int:
        """
        Retorna a pontuação do oponente.
        """
        return self.opponent_score

    def get_hand_points(self) -> int:
        """
        Retorna a quantidade de pontos em disputa.
        """
        return self.hand_points

    @classmethod
    def from_dict(cls, data: dict) -> 'GameIntel':
        return cls(
            cards=[TrucoCard.from_dict(card) for card in data["cards"]],
            open_cards=[TrucoCard.from_dict(card) for card in data.get("openCards", [])],
            vira=TrucoCard.from_dict(data["vira"]),
            opponent_card=TrucoCard.from_dict(data["opponentCard"]) if data.get("opponentCard") else None,
            round_results=data.get("roundResults", []),
            score=data["score"],
            opponent_score=data["opponentScore"],
            hand_points=data["handPoints"]
        )

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, GameIntel):
            return False
        return (self.score == other.score and
                self.opponent_score == other.opponent_score and
                self.hand_points == other.hand_points and
                self.cards == other.cards and
                self.open_cards == other.open_cards and
                self.vira == other.vira and
                self.opponent_card == other.opponent_card and
                self.round_results == other.round_results)

    def __hash__(self):
        return hash((tuple(self.cards), tuple(self.open_cards), self.vira, self.opponent_card,
                     tuple(self.round_results), self.score, self.opponent_score, self.hand_points))


def extract_features(game_intel: GameIntel):
    """
    Converte os atributos de GameIntel em um vetor de features numérico.
    """
    # Converte cartas para valores numéricos
    cards_features = [card.to_numeric() for card in game_intel.get_cards()]
    open_cards_features = [card.to_numeric() for card in game_intel.get_open_cards()]
    vira_feature = game_intel.get_vira().to_numeric()
    
    # Converte os resultados das rodadas para valores numéricos (1 = vitória, 0 = derrota/empate)
    round_results_encoded = [1 if res == GameIntel.RoundResult.WON else 0 for res in game_intel.get_round_results()]
    
    # Obtém valores inteiros de placar e pontos
    score = game_intel.get_score()
    opponent_score = game_intel.get_opponent_score()
    hand_points = game_intel.get_hand_points()

    # Junta tudo em um único vetor de entrada
    features = cards_features + open_cards_features + [vira_feature] + round_results_encoded + [score, opponent_score, hand_points]
    
    # return np.array(features, dtype=np.float32)
    return features  # Temporário: retorna lista em vez de array NumPy
