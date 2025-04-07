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
    players = PlayerSerializer(many=True)
    currentPlayerUuid = serializers.CharField()
    # Campo opcional, pois pode não vir na requisição
    openCards = TrucoCardSerializer(many=True, required=False, default=[])
    vira = TrucoCardSerializer()
    # Campo opcional, se não houver carta para jogar contra
    cardToPlayAgainst = TrucoCardSerializer(required=False, allow_null=True)
    roundWinnersUuid = serializers.ListField(
        child=serializers.CharField(), required=False, default=[]
    )
    currentPlayerScore = serializers.IntegerField()
    currentOpponentScore = serializers.IntegerField()
    handPoints = serializers.IntegerField()

    def create(self, validated_data):
        # Aqui você pode converter os dados validados para uma instância de GameIntel.
        # Basta utilizar o método from_dict da sua classe.
        from bot.game_model.game_intel import GameIntel  # ajuste o caminho conforme necessário
        return GameIntel.from_dict(validated_data)