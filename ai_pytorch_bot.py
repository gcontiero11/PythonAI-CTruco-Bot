import torch
from bot.game_model.game_intel import extract_features

class Ai:
    # ...existing code...

    def choose_card(self, game_intel: GameIntel):
        """
        Escolhe a melhor carta com base no estado atual do jogo.
        """
        features = extract_features(game_intel)
        features = torch.tensor(features, dtype=torch.float32).unsqueeze(0)  # Adiciona batch dimension
        
        with torch.no_grad():
            predictions = self.model(features)
        
        best_card_index = torch.argmax(predictions).item()
        
        return game_intel.get_cards()[best_card_index]
