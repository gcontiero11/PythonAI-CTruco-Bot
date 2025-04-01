import threading
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from typing import List, Optional
from bot.game_model.game_intel import GameIntel
from bot.game_model.card_to_play import CardToPlay
from bot.game_model.interfaces import BotServiceProvider

class DjangoRemoteBot:
    """
    Bot para jogar Truco usando redes neurais para cada decisão:
      - get_mao_de_onze_response: decide se vai para mão de onze (True/False)
      - decide_if_raises: decide se aumenta a aposta (True/False)
      - choose_card: escolhe a carta a ser jogada (baseado em um índice)
      - get_raise_response: escolhe a resposta ao aumento (-1, 0 ou 1)
    """
    def __init__(self):
        self.input_dim = 20  # número de features; ajuste conforme seu pré-processamento

        # Criação dos modelos para cada tarefa
        self.model_mao_onze = self.build_binary_model()
        self.model_raise = self.build_binary_model()  # Para decide_if_raises
        self.model_choose_card = self.build_card_model(num_classes=10)  # supondo 10 cartas possíveis
        self.model_raise_response = self.build_raise_response_model()

    def build_binary_model(self):
        model = keras.Sequential([
            layers.Dense(32, activation='relu', input_shape=(self.input_dim,)),
            layers.Dense(16, activation='relu'),
            layers.Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def build_card_model(self, num_classes):
        model = keras.Sequential([
            layers.Dense(32, activation='relu', input_shape=(self.input_dim,)),
            layers.Dense(16, activation='relu'),
            layers.Dense(num_classes, activation='softmax')
        ])
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        return model

    def build_raise_response_model(self):
        model = keras.Sequential([
            layers.Dense(32, activation='relu', input_shape=(self.input_dim,)),
            layers.Dense(16, activation='relu'),
            layers.Dense(3, activation='softmax')
        ])
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        return model

    def extract_features(self, intel: GameIntel):
        """
        Extrai as features do GameIntel.
        Para este exemplo, supomos que intel possui um atributo 'features' (lista ou array)
        com self.input_dim elementos. Caso não exista, você deve implementar a extração das features
        a partir dos demais atributos (como pontuação, quantidade de cartas, etc.).
        """
        # Exemplo: se não houver atributo 'features', poderíamos concatenar informações relevantes.
        # Aqui, usaremos um vetor aleatório para simulação.
        features = getattr(intel, 'features', np.random.rand(self.input_dim))
        features = np.array(features, dtype=np.float32)
        return features.reshape(1, -1)

    def get_mao_de_onze_response(self, intel: GameIntel) -> bool:
        features = self.extract_features(intel)
        prob = self.model_mao_onze.predict(features, verbose=0)
        decision = prob[0][0] > 0.5
        print(f"[get_mao_de_onze_response] Prob: {prob[0][0]:.4f} -> Decision: {decision}")
        return decision

    def decide_if_raises(self, intel: GameIntel) -> bool:
        features = self.extract_features(intel)
        prob = self.model_raise.predict(features, verbose=0)
        decision = prob[0][0] > 0.5
        print(f"[decide_if_raises] Prob: {prob[0][0]:.4f} -> Decision: {decision}")
        return decision

    def choose_card(self, intel: GameIntel) -> CardToPlay:
        features = self.extract_features(intel)
        predictions = self.model_choose_card.predict(features, verbose=0)
        card_index = np.argmax(predictions)
        if card_index >= len(intel.cards):
            card_index = 0  # fallback
        chosen_card = intel.cards[card_index]
        print(f"[choose_card] Predictions: {predictions[0]}, Chosen index: {card_index}, Card: {chosen_card}")
        return CardToPlay.of(chosen_card)

    def get_raise_response(self, intel: GameIntel) -> int:
        features = self.extract_features(intel)
        predictions = self.model_raise_response.predict(features, verbose=0)
        class_pred = np.argmax(predictions)
        mapping = {0: -1, 1: 0, 2: 1}
        decision = mapping.get(class_pred, 0)
        print(f"[get_raise_response] Predictions: {predictions[0]}, Mapped decision: {decision}")
        return decision