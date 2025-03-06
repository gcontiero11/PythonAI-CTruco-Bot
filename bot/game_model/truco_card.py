from django.db import models
from bot.game_model.enums import CardRank, CardSuit
import threading 

'''
<p>Represents a valid truco card described in terms of a {@link CardRank} and a {@link CardSuit}. It also
encompasses a method to compare its value based on a vira card, as well as methods to check if the card is
considered a manilha (zap, copas, espadilha or ouros) based on such vira. Objects of this class are final,
cached, and must be created using the static constructors  {@link #of(CardRank rank, CardSuit suit)} or
{@link #closed()}.
'''
class TrucoCard:
    _cache_lock = threading.Lock()
    _cache = {}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    '''
    /**
    * <p>Creates a value object representing a Truco card.
    * The returned card is final and cached, therefore two cards of same value are represented by the same object.
    * This method does not allow creating a card that has a hidden rank and non-hidden suit or vice-versa. Use the
    * {@link #TrucoCard closed()} method to create a closed card that represents a discard.
    * </p>
    *
    * @param rank a card rank represented by the CardRank enum, must be non-null
    * @param suit a card suit represented by the CardSuit enum, must be non-null
    * @return a TrucoCard representing the given {@code rank} and {@code suit}
    * @throws NullPointerException if {@code rank} or/and {@code suit} is/are null
    * @throws IllegalArgumentException if rank or suit is HIDDEN and the other parameter is not HIDDEN
    */
    '''
    @staticmethod
    def of(rank, suit):
        # Usa a trava para garantir que apenas um thread acessa o cache por vez
        with TrucoCard._cache_lock:
            # Gera a chave do cache com base no valor do rank e suit
            cache_key = (rank.value(), suit.value())
            
            if cache_key not in TrucoCard._cache:
                TrucoCard._cache[cache_key] = TrucoCard(rank, suit)

            return TrucoCard._cache[cache_key]

    '''
    /**
    * <p>Creates a value object representing a closed Truco card.
    * The returned card is final and cached, therefore two closed cards are represented by the same object.
    * </p>
    *
    * @return TrucoCard representing a closed card, i.e., a discard
    */
    '''
    @staticmethod
    def closed():
        # Retorna a carta fechada, que é um caso especial no truco
        return TrucoCard.of(CardRank.HIDDEN, CardSuit.HIDDEN)

    '''
    /**
    * <p>Compares two TrucoCard objects based on their relative values defined using the {@code vira} card parameter.
    * Examples:
    * </p>
    * <pre>{@code
    *    TrucoCard.of(CardRank.FIVE, CardSuit.CLUBS)
    *       .compareValueTo(TrucoCard.of(CardRank.FOUR, CardSuit.CLUBS),
    *           TrucoCard.of(CardRank.SIX, CardSuit.CLUBS)) returns positive;
    *
    *    TrucoCard.of(CardRank.FOUR, CardSuit.SPADES)
    *       .compareValueTo(TrucoCard.of(CardRank.FOUR, CardSuit.CLUBS),
    *           TrucoCard.of(CardRank.SIX, CardSuit.CLUBS)) returns 0;
    *
    *    TrucoCard.of(CardRank.THREE, CardSuit.CLUBS)
    *       .compareValueTo(TrucoCard.of(CardRank.SIX, CardSuit.CLUBS),
    *          TrucoCard.of(CardRank.FIVE, CardSuit.CLUBS)) returns negative,
    *          because TrucoCard.of(CardRank.SIX, CardSuit.CLUBS) is the zap.
    *    }
    * </pre>
    * <p>
    * Notice that cards of same rank and different suits can have the same relative value if they are not manilhas,
    * but they still different according to the {@link #equals(Object o)} method.
    * </p>
    *
    * @param otherCard TrucoCard to be compared to the reference, must be non-null
    * @param vira TrucoCard representing the current vira, must be non-null
    * @return returns a positive number if the TrucoCard represented by the object is greater than the
    * {@code otherCard}, a negative number if the object card is lower, and 0 if both cards have the same
    * relative value. The returned value is the difference between the values of the compared cards.
    * @throws NullPointerException if {@code otherCard} or/and {@code vira} is/are null.
    */
    '''
    def compare_value_to(self, other_card: 'TrucoCard', vira: 'TrucoCard') -> int:
        if other_card is None or vira is None:
            raise ValueError("Other card and vira cannot be None.")
        return self.relative_value(vira) - other_card.relative_value(vira)

    '''
    /**
    * <p>Get the relative card value based on the current {@code vira} card parameter.</p>
    *
    * @param vira TrucoCard representing the current vira, must be non-null.
    * @return It returns 0 if the card is hidden. Returns 13 for zap, 12 for copas, 11 for espadilha, and 10 for ouros.
    * If the card is not hidden nor manilha, returns a value based on the card rank value and the {@code vira} rank
    * value. For instance, if the card rank is 4 and the vira rank is 7, then the relative card value is 1 (the lowest
    * card value for an open card). If the card rank is 7 and the vira rank is 4, then the relative card value is 3 —
    * because the absolute value for rank 7 is 4, but the rank 5 is for manilhas and does not count in the sequence.
    * @throws NullPointerException if {@code vira} is null.
    */
    '''
    def relative_value(self, vira: 'TrucoCard') -> int:
        if self.is_manilha(vira):
            return {
                "DIAMONDS": 10,
                "SPADES": 11,
                "HEARTS": 12,
                "CLUBS": 13
            }[self.suit.name]
        if self.rank.value == 0:
            return 0
        return self.rank.value - 1 if self.rank.value > vira.rank.value else self.rank.value
      
    '''
    /**
    * <p>Checks if the truco card represented by the object is a manilha using the {@code vira} card parameter.</p>
    * <pre>{@code
    *    //Returns true because the object relative value is
    *    //a manilha (zap) based on the vira parameter
    *    TrucoCard.of(CardRank.FIVE, CardSuit.CLUBS)
    *       .isManilha(TrucoCard.of(CardRank.FOUR, CardSuit.CLUBS));
    *    }
    * @param vira TrucoCard representing the current vira, must be non-null
    * @return true if the object is a manilha because of the {@code vira} card parameter and false otherwise
    * @throws NullPointerException if {@code vira} is null
    */
    '''
    def is_manilha(self, vira: 'TrucoCard') -> bool:
        return self.rank == vira.rank.next()

    
    '''
    /**
     * <p>Checks if the truco card represented by the object is a zap using the {@code vira} card parameter.</p>
     * <pre>{@code
     *    //Returns true because the object relative value is
     *    //a zap based on the vira parameter
     *    TrucoCard.of(CardRank.FIVE, CardSuit.CLUBS)
     *       .isZap(TrucoCard.of(CardRank.FOUR, CardSuit.CLUBS));
     *    }
     * @param vira TrucoCard representing the current vira, must be non-null
     * @return true if the object is a zap because of the {@code vira} card parameter and false otherwise
     * @throws NullPointerException if {@code vira} is null
     */
    '''
    def is_zap(self, vira: 'TrucoCard') -> bool:
        return self.is_manilha(vira) and self.suit.name == "CLUBS"
    
    '''
    /**
     * <p>Checks if the truco card represented by the object is a copas using the {@code vira} card parameter.</p>
     * <pre>{@code
     *    //Returns true because the object relative value is
     *    //a copas based on the vira parameter
     *    TrucoCard.of(CardRank.FIVE, CardSuit.HEARTS)
     *       .isCopas(TrucoCard.of(CardRank.FOUR, CardSuit.CLUBS));
     *    }
     * @param vira TrucoCard representing the current vira, must be non-null
     * @return true if the object is a copas because of the {@code vira} card parameter and false otherwise
     * @throws NullPointerException if {@code vira} is null
     */
    '''
    def is_copas(self, vira: 'TrucoCard') -> bool:
        return self.is_manilha(vira) and self.suit.name == "HEARTS"

    '''
    /**
     * <p>Checks if the truco card represented by the object is an espadilha using the {@code vira} card parameter.</p>
     * <pre>{@code
     *    //Returns true because the object relative value is
     *    //an espadilha based on the vira parameter
     *    TrucoCard.of(CardRank.FIVE, CardSuit.SPADES)
     *       .isEspadilha(TrucoCard.of(CardRank.FOUR, CardSuit.CLUBS));
     *    }
     * @param vira TrucoCard representing the current vira, must be non-null
     * @return true if the object is an espadilha because of the {@code vira} card parameter and false otherwise
     * @throws NullPointerException if {@code vira} is null
     */
    '''
    def is_espadilha(self, vira: 'TrucoCard') -> bool:
        return self.is_manilha(vira) and self.suit.name == "SPADES"

    
    '''
    /**
     * <p>Checks if the truco card represented by the object is an ouros using the {@code vira} card parameter.</p>
     * <pre>{@code
     *    //Returns true because the object relative value is
     *    //an ouros based on the vira parameter
     *    TrucoCard.of(CardRank.FIVE, CardSuit.DIAMONDS)
     *       .isOuros(TrucoCard.of(CardRank.FOUR, CardSuit.CLUBS));
     *    }
     * @param vira TrucoCard representing the current vira, must be non-null
     * @return true if the object is an ouros because of the {@code vira} card parameter and false otherwise
     * @throws NullPointerException if {@code vira} is null
     */
    '''
    def is_ouros(self, vira: 'TrucoCard') -> bool:
        return self.is_manilha(vira) and self.suit.name == "DIAMONDS"
    
    @classmethod
    def from_dict(cls, data: dict) -> 'TrucoCard':
        return cls(
            rank=data["rank"],  
            suit=data["suit"]
        )

    def __eq__(self, other):
        if not isinstance(other, TrucoCard):
            return False
        return self.rank == other.rank and self.suit == other.suit

    def __repr__(self):
        return f"[{self.rank}, {self.suit}]"