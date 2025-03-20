# PythonAI-CTruco-Bot

Este projeto implementa um bot de inteligência artificial para jogar Truco Paulista usando redes neurais treinadas com PyTorch. O bot analisa jogadas, aprende com as partidas e toma decisões estratégicas para maximizar suas chances de vitória.

## 🛠 Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto
- **PyTorch**: Framework para redes neurais
- **Django**: Integração com o ambiente do jogo
- **Machine Learning**: Treinamento do bot para melhorar suas jogadas

## 📌 Funcionalidades
- **Escolha da Melhor Carta**: O bot decide qual carta jogar com base em uma rede neural.
- **Decisão de Truco**: O bot avalia se deve pedir Truco, aceitar ou fugir da rodada.
- **Aprendizado Contínuo**: Ajusta sua estratégia conforme joga contra diferentes adversários.

## 🚀 Como Executar o Projeto
1. Clone este repositório:
   ```bash
   git clone https://github.com/RaFeltrim/PythonAI-CTruco-Bot.git
   ```
2. Instale as dependências:
   ```bash
   pip install torch django
   ```
3. Execute o bot no ambiente de jogo:
   ```bash
   python run_bot.py
   ```

## 🧠 Estrutura do Código
- `bot/game_model/` → Contém as classes que modelam o jogo
- `bot/neural_networks.py` → Definição das redes neurais para tomada de decisão
- `bot/DjangoRemoteBot.py` → Implementação do bot com machine learning

## 🎯 Próximos Passos
- Melhorar o treinamento da IA com mais dados de partidas reais
- Implementar estratégias avançadas de blefe e adaptação ao estilo do oponente
- Testes e otimizações para desempenho

## 🤝 Contribuição
Sinta-se à vontade para abrir issues e pull requests com sugestões de melhorias!

Desenvolvido por Rafael Feltrim, Gustavo Gomes Contiero, Heitor Lemes Caldas 🤖
