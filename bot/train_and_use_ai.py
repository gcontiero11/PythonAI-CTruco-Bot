from bot.game_model.game_intel import GameIntel
from bot.game_model.card_to_play import CardToPlay
from ai_torch_bot import Ai  # Supondo que a classe Ai esteja em um arquivo chamado ai.py

# Exemplo de dados de treinamento (substitua pelos seus dados reais)
training_data = [
    ([0.1, 0.2, 0.3], 0),
    ([0.4, 0.5, 0.6], 1),
    # Adicione mais dados conforme necessário
]

# Inicialize a AI
input_channels = 3  # Número de recursos de entrada
num_classes = 2  # Número de classes de saída (por exemplo, 2 classes: 0 e 1)
ai = Ai(input_channels, num_classes)

# Treine a AI
ai.train(training_data, epochs=500)

# Exemplo de uso da AI para fazer previsões
intel = GameIntel()  # Supondo que você tenha uma instância da classe GameIntel
card_to_play = ai.choose_card(intel)
print(f"Card to play: {card_to_play}")

# Salvar o modelo treinado
ai.save_model("modelo_treinado.pth")

# Carregar o modelo treinado
ai.load_model("modelo_treinado.pth")