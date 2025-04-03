import unittest
import numpy as np
from bot.train_and_use_ai import Ai
from bot.game_model.game_intel import GameIntel
from bot.game_model.card_to_play import CardToPlay

class TestAi(unittest.TestCase):
    def setUp(self):
        self.input_dim = 3
        self.num_classes = 2
        self.ai = Ai(self.input_dim, self.num_classes)

    def test_model_building(self):
        self.assertIsNotNone(self.ai.model)
        self.assertEqual(len(self.ai.model.layers), 3)

    def test_training(self):
        training_data = [
            ([0.1, 0.2, 0.3], 0),
            ([0.4, 0.5, 0.6], 1),
        ]
        self.ai.train(training_data, epochs=1)  # Train for 1 epoch for testing
        self.assertTrue(self.ai.model.history.history['loss'])

    def test_choose_card(self):
        class DummyGameIntel(GameIntel):
            def __init__(self):
                self.cards = ['Card1', 'Card2']
            
            def get_features(self):
                return [0.2, 0.3, 0.4]

        intel = DummyGameIntel()
        card_to_play = self.ai.choose_card(intel)
        self.assertIn(card_to_play, intel.cards)

if __name__ == '__main__':
    unittest.main()