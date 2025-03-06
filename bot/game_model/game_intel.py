from typing import List, Optional
from bot.game_model.truco_card import TrucoCard


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
        current_player = next(
            (p for p in data["players"] if p["uuid"] == data["currentPlayerUuid"]), None
        )

        if not current_player:
            raise ValueError("Current Player not found")

        return cls(
            cards=[TrucoCard.from_dict(card) for card in current_player["cards"]],
            open_cards=[TrucoCard.from_dict(card) for card in data.get("openCards", [])],
            vira=TrucoCard.from_dict(data["vira"]),
            opponent_card=TrucoCard.from_dict(data["cardToPlayAgainst"]) if data.get("cardToPlayAgainst") else None,
            round_results=data.get("roundWinnersUuid", []),
            score=data["currentPlayerScore"],
            opponent_score=data["currentOpponentScore"],
            hand_points=data["handPoints"]
        )

    class StepBuilder:
        def __init__(self):
            self.cards = None
            self.open_cards = None
            self.vira = None
            self.opponent_card = None
            self.round_results = None
            self.score = 0
            self.opponent_score = 0
            self.hand_points = 0

        @staticmethod
        def with_():
            return GameIntel.StepBuilder()

        def game_info(self, round_results: List[str], open_cards: List['TrucoCard'], vira: 'TrucoCard', hand_points: int):
            self.round_results = round_results.copy()
            self.open_cards = open_cards.copy()
            self.vira = vira
            self.hand_points = hand_points
            return self

        def bot_info(self, cards: List['TrucoCard'], score: int):
            self.cards = cards
            self.score = score
            return self

        def opponent_score(self, opponent_score: int):
            self.opponent_score = opponent_score
            return self

        def opponent_card(self, card: 'TrucoCard'):
            """
            Passo opcional do builder. Define a carta do oponente, caso exista.
            """
            self.opponent_card = card
            return self

        def build(self) -> 'GameIntel':
            """
            Conclui o processo de construção e retorna o objeto GameIntel.
            """
            return GameIntel(self.cards, self.open_cards, self.vira, self.opponent_card, self.round_results,
                             self.score, self.opponent_score, self.hand_points)

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
