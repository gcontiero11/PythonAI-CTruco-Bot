from rest_framework import serializers

class TrucoCardSerializer(serializers.Serializer):
    # Considerando que rank e suit são enviados como strings. 
    # Caso sejam números ou outro tipo, ajuste os tipos abaixo.
    rank = serializers.CharField()
    suit = serializers.CharField()

class PlayerSerializer(serializers.Serializer):
    uuid = serializers.CharField()
    cards = TrucoCardSerializer(many=True)

class GameIntelSerializer(serializers.Serializer):
    cards = TrucoCardSerializer(many=True)
    openCards = TrucoCardSerializer(many=True, required=False, default=[])
    vira = TrucoCardSerializer()
    opponentCard = TrucoCardSerializer(required=False, allow_null=True)
    roundResults = serializers.ListField(
        child=serializers.CharField(), required=False, default=[]
    )
    score = serializers.IntegerField()
    opponentScore = serializers.IntegerField()
    handPoints = serializers.IntegerField()

    def create(self, validated_data):
        from bot.game_model.game_intel import GameIntel
        return GameIntel.from_dict(validated_data)