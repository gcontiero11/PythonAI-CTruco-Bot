import unittest
from bot.game_model.game_intel import GameIntel
from bot.game_model.card_to_play import CardToPlay

class TestGameIntel(unittest.TestCase):
    def setUp(self):
        self.intel = GameIntel()
        self.intel.cards = ['Card1', 'Card2', 'Card3']

    def test_get_features(self):
        features = self.intel.get_features()
        self.assertEqual(len(features), 3)  # Assuming 3 features for the test

class TestCardToPlay(unittest.TestCase):
    def test_card_creation(self):
        card = CardToPlay.of('Card1')
        self.assertEqual(card.name, 'Card1')  # Assuming CardToPlay has a name attribute

if __name__ == '__main__':
    unittest.main()