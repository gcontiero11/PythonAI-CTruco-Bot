from bot.game_model.truco_card import TrucoCard

class CardToPlay:
    def __init__(self, card, discard):
        if card is None:
            raise ValueError("The card must not be null.")
        self.content = card
        self.discard = discard

    @staticmethod
    def of(card):
        """
        Representa a carta que será jogada na rodada. O objeto retornado é final
        e sempre retornará False quando isDiscard() for invocado.
        
        :param card: uma TrucoCard que será jogada, deve ser não-nula.
        :return: um objeto CardToPlay representando a TrucoCard a ser jogada.
        """
        return CardToPlay(card, False)

    @staticmethod
    def discard(card):
        """
        Representa a carta que será descartada na rodada. O objeto retornado é final
        e sempre retornará True quando isDiscard() for invocado.
        
        :param card: uma TrucoCard que será descartada, deve ser não-nula.
        :return: um objeto CardToPlay representando a TrucoCard a ser descartada.
        """
        return CardToPlay(card, True)

    def value(self):
        """
        Retorna a TrucoCard embrulhada, que será jogada ou TrucoCard.closed()
        se a carta for descartada.
        
        :return: TrucoCard a ser jogada ou TrucoCard.closed() se descartada.
        """
        return TrucoCard.closed() if self.discard else self.content

    def content(self):
        """
        Retorna o objeto TrucoCard usado para criar o CardToPlay.
        
        :return: o mesmo objeto TrucoCard usado para criar o CardToPlay.
        """
        return self.content

    def is_discard(self):
        """
        Indica se o CardToPlay é para ser descartado ou não.
        
        :return: True se a carta é para ser descartada, False caso contrário.
        """
        return self.discard

    def __str__(self):
        return f"CardToPlay(content={self.content}, discard={self.discard})"

    def __eq__(self, other):
        """
        Compara a igualdade dos objetos com base no conteúdo e tipo de carta (descartada ou não).
        
        :param other: outro objeto a ser comparado.
        :return: True se os objetos forem iguais, False caso contrário.
        """
        if self is other:
            return True
        if not isinstance(other, CardToPlay):
            return False
        return self.discard == other.discard and self.content == other.content

    def __hash__(self):
        """
        Gera o código hash para o objeto baseado no conteúdo e tipo de carta.
        
        :return: código hash baseado no conteúdo e tipo da carta.
        """
        return hash((self.content, self.discard))

    def to_dict(self):
        """
        Converte o objeto CardToPlay para um dicionário.
        """
        return {
            "content": {
                "rank": self.content.rank,
                "suit": self.content.suit
            },
            "discard": self.discard
        }