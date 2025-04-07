# import numpy as np
# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers

# Importações do projeto
from bot.game_model.game_intel import GameIntel
from bot.game_model.card_to_play import CardToPlay

class Ai:
    def __init__(self, input_dim, num_classes):
        self.input_dim = input_dim
        self.num_classes = num_classes
        # self.model = self.build_model()

    # def build_model(self):
    #     model = keras.Sequential([
    #         layers.Dense(32, activation='relu', input_shape=(self.input_dim,)),
    #         layers.Dense(16, activation='relu'),
    #         layers.Dense(self.num_classes, activation='softmax')
    #     ])
    #     model.compile(optimizer='adam',
    #                   loss='sparse_categorical_crossentropy',
    #                   metrics=['accuracy'])
    #     return model

    # def train(self, training_data, epochs=500):
    #     # training_data é uma lista de tuplas (features, label)
    #     X, y = zip(*training_data)
    #     X = np.array(X, dtype=np.float32)
    #     y = np.array(y, dtype=np.int32)
    #     self.model.fit(X, y, epochs=epochs, batch_size=32, validation_split=0.2, verbose=1)

    def choose_card(self, intel: GameIntel) -> CardToPlay:
        # Assume que intel.get_features() retorna uma lista ou array com dimensão igual a input_dim.
        # features = np.array(intel.get_features(), dtype=np.float32).reshape(1, -1)
        # predictions = self.model.predict(features, verbose=0)
        # card_index = np.argmax(predictions)
        # Cria a jogada utilizando o índice previsto e a lista de cartas em intel.
        # return CardToPlay.of(intel.cards[card_index])
        if not intel.cards:
            return None
        return CardToPlay.of(intel.cards[0])  # Temporário: sempre escolhe a primeira carta

    # def save_model(self, path):
    #     self.model.save(path)

    # def load_model(self, path):
    #     self.model = keras.models.load_model(path)

# Exemplo de dados de treinamento (substitua pelos seus dados reais)
training_data = [
    ([0.1, 0.2, 0.3], 0),
    ([0.4, 0.5, 0.6], 1),
    # Adicione mais dados conforme necessário
]

if __name__ == '__main__':
    # Inicializa a AI com as dimensões apropriadas
    input_dim = 3      # Número de recursos de entrada
    num_classes = 2    # Número de classes de saída (ex.: 2 classes: 0 e 1)
    ai = Ai(input_dim, num_classes)

    # Treina a AI com os dados fornecidos
    # ai.train(training_data, epochs=500)

    # Exemplo de uso da AI para fazer previsões.
    # Se GameIntel não estiver implementado para testes, vamos criar uma classe dummy.
    class DummyGameIntel(GameIntel):
        def __init__(self):
            # Exemplo de lista de cartas; adapte conforme sua implementação real.
            self.cards = ['Card1', 'Card2']
        
        def get_features(self):
            # Retorna um vetor de features com dimensão igual a input_dim.
            return [0.2, 0.3, 0.4]
    
    intel = DummyGameIntel()
    card_to_play = ai.choose_card(intel)
    print(f"Card to play: {card_to_play}")

    # Salva o modelo treinado (usando extensão .h5 para TensorFlow)
    # model_path = "modelo_treinado.h5"
    # ai.save_model(model_path)
    # print(f"Modelo salvo em '{model_path}'.")

    # Carrega o modelo treinado
    # ai.load_model(model_path)
    # print("Modelo carregado com sucesso.")