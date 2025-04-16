from django.db import models
from bot.game_model.truco_card import TrucoCard
from bot.game_model.game_intel import GameIntel

class GameIntelModel(models.Model):
    # Decision information
    DECISION_TYPES = [
        ('mao_de_onze', 'Mão de Onze'),
        ('decide_if_raises', 'Decide If Raises'),
        ('choose_card', 'Choose Card'),
        ('get_raise_response', 'Get Raise Response'),
    ]
    decision_type = models.CharField(max_length=20, choices=DECISION_TYPES, default='choose_card')
    decision_result = models.JSONField(null=True)  # Store the result of the decision
    
    # Cards in hand
    cards = models.JSONField()  # Will store list of cards as JSON
    
    # Open cards on table
    open_cards = models.JSONField(default=list)  # Will store list of open cards as JSON
    
    # Vira card
    vira = models.JSONField()  # Will store single card as JSON
    
    # Opponent's card (optional)
    opponent_card = models.JSONField(null=True, blank=True)  # Will store single card as JSON
    
    # Round results
    round_results = models.JSONField(default=list)  # Will store list of results as JSON
    
    # Scores
    score = models.IntegerField(default=0)
    opponent_score = models.IntegerField(default=0)
    hand_points = models.IntegerField(default=1)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_game_intel(self) -> 'GameIntel':
        """Convert model instance back to GameIntel object"""
        from bot.game_model.game_intel import GameIntel
        return GameIntel(
            cards=[TrucoCard.from_dict(card) for card in self.cards],
            open_cards=[TrucoCard.from_dict(card) for card in self.open_cards],
            vira=TrucoCard.from_dict(self.vira),
            opponent_card=TrucoCard.from_dict(self.opponent_card) if self.opponent_card else None,
            round_results=self.round_results,
            score=self.score,
            opponent_score=self.opponent_score,
            hand_points=self.hand_points
        )

    @classmethod
    def from_game_intel(cls, game_intel: 'GameIntel', decision_type: str = None, decision_result: any = None) -> 'GameIntelModel':
        """Create model instance from GameIntel object"""
        return cls(
            cards=[card.to_dict() for card in game_intel.cards],
            open_cards=[card.to_dict() for card in game_intel.open_cards],
            vira=game_intel.vira.to_dict(),
            opponent_card=game_intel.opponent_card.to_dict() if game_intel.opponent_card else None,
            round_results=game_intel.round_results,
            score=game_intel.score,
            opponent_score=game_intel.opponent_score,
            hand_points=game_intel.hand_points,
            decision_type=decision_type,
            decision_result=decision_result
        )

# Get all decisions made in a game
decisions = GameIntelModel.objects.all().order_by('created_at')

# Get all card choices
card_choices = GameIntelModel.objects.filter(decision_type='choose_card')

# Get all raise decisions
raise_decisions = GameIntelModel.objects.filter(decision_type='decide_if_raises') 