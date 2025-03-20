import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from bot.game_model.game_intel import GameIntel
from bot.game_model.card_to_play import CardToPlay

class ConvolutionalNeuralNetwork(nn.Module):
    def __init__(self, input_channels, num_classes):
        super(ConvolutionalNeuralNetwork, self).__init__()
        self.conv1 = nn.Conv1d(input_channels, 128, kernel_size=3, stride=1, padding=1)
        self.relu = nn.ReLU()
        self.fc = nn.Linear(128, num_classes)
    
    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x

class Ai:
    def __init__(self, input_channels, num_classes):
        self.model = ConvolutionalNeuralNetwork(input_channels, num_classes)
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)
    
    def train(self, training_data, epochs=1000):
        X, y = zip(*training_data)
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)
        
        for epoch in range(epochs):
            self.model.train()
            inputs = torch.tensor(X_train, dtype=torch.float32)
            labels = torch.tensor(y_train, dtype=torch.long)
            outputs = self.model(inputs)
            loss = self.criterion(outputs, labels)
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

            if epoch % 100 == 0:
                self.model.eval()
                val_inputs = torch.tensor(X_val, dtype=torch.float32)
                val_labels = torch.tensor(y_val, dtype=torch.long)
                val_outputs = self.model(val_inputs)
                val_loss = self.criterion(val_outputs, val_labels)
                print(f'Epoch {epoch}, Loss: {loss.item()}, Val Loss: {val_loss.item()}')
    
    def choose_card(self, intel: GameIntel) -> CardToPlay:
        input_tensor = torch.tensor(intel.get_features(), dtype=torch.float32).unsqueeze(0)
        output = self.model(input_tensor)
        _, predicted = torch.max(output.data, 1)
        return CardToPlay(intel.cards[predicted.item()], False)
    
    def decide_if_raises(self, intel: GameIntel) -> bool:
        input_tensor = torch.tensor(intel.get_features(), dtype=torch.float32).unsqueeze(0)
        output = self.model(input_tensor)
        _, predicted = torch.max(output.data, 1)
        return predicted.item() == 1
    
    def get_raise_response(self, intel: GameIntel) -> int:
        input_tensor = torch.tensor(intel.get_features(), dtype=torch.float32).unsqueeze(0)
        output = self.model(input_tensor)
        _, predicted = torch.max(output.data, 1)
        return predicted.item() - 1  # -1 for fugir, 0 for aceitar, 1 for aumentar

    def save_model(self, path):
        torch.save(self.model.state_dict(), path)
    
    def load_model(self, path):
        self.model.load_state_dict(torch.load(path))