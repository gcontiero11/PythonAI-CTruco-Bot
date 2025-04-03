# PythonAI-CTruco-Bot

## Overview
PythonAI-CTruco-Bot is an AI-powered bot designed to play Truco Paulista, a popular card game in Brazil. The bot utilizes machine learning techniques to make decisions based on game intelligence and features extracted from the game state.

## Features
- AI model built using TensorFlow for decision-making.
- Ability to train the model with custom training data.
- Integration with game intelligence to evaluate the best card to play.
- Model saving and loading capabilities for persistent learning.

## Project Structure
```
PythonAI-CTruco-Bot
├── bot
│   ├── __init__.py
│   ├── train_and_use_ai.py
│   ├── game_model
│   │   ├── __init__.py
│   │   ├── game_intel.py
│   │   └── card_to_play.py
├── data
│   ├── training_data.json
│   └── test_data.json
├── models
│   └── modelo_treinado.h5
├── tests
│   ├── __init__.py
│   ├── test_ai.py
│   └── test_game_model.py
├── requirements.txt
└── README.md
```

## Installation
To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd PythonAI-CTruco-Bot
pip install -r requirements.txt
```

## Usage
1. Prepare your training data in `data/training_data.json`.
2. Run the AI training script:

```bash
python bot/train_and_use_ai.py
```

3. The trained model will be saved as `models/modelo_treinado.h5`.

4. You can modify the `train_and_use_ai.py` file to customize the training process or the AI's decision-making logic.

## Testing
To ensure the functionality of the AI bot and game model components, run the tests located in the `tests` directory:

```bash
python -m unittest discover -s tests
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.