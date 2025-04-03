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

Explicação dos Principais Pontos
Classe Ai:

Cria um modelo Keras simples com duas camadas densas e uma camada final com ativação softmax.

O método train utiliza dados de treinamento fornecidos na forma de uma lista de tuplas (features, label).

O método choose_card realiza uma predição com base nas features extraídas do objeto GameIntel e seleciona o índice com maior probabilidade para buscar a carta correspondente.

Dados de Treinamento:

Os dados de exemplo são definidos manualmente. Para uso real, você deve substituir por um dataset consistente com a sua aplicação.

Integração com Django:

Este script pode ser adaptado para ser executado como um comando de gerenciamento Django (por exemplo, em bot/management/commands/train_bot.py) caso deseje integrá-lo ao ambiente web.

Salvamento e Carregamento do Modelo:

O modelo é salvo em formato HDF5 (.h5) e pode ser recarregado para uso posterior.

Esse script permite treinar, testar e persistir seu modelo de AI utilizando TensorFlow, integrando-o com os componentes do seu projeto. Adapte os detalhes (como a extração de features e o dataset) conforme a lógica do seu jogo.

## Como rodar o train

Verifique as Dependências:
Certifique-se de que todas as bibliotecas necessárias estão instaladas. Se você tiver um arquivo requirements.txt, execute:

bash
Copiar
Editar
pip install -r requirements.txt
Caso não tenha, garanta que o TensorFlow, NumPy e as demais dependências (como Django, se estiver integrado) estejam instaladas.

Configure o Ambiente:
Se estiver usando um ambiente virtual (recomendado), ative-o antes de instalar as dependências e executar o script.

Estrutura do Projeto:
Certifique-se de que o script train_and_use_ai.py esteja no diretório correto e que os imports (como from bot.game_model.game_intel import GameIntel) apontem para os locais corretos no seu projeto.

Execute o Script:
No terminal, navegue até a pasta raiz do seu projeto e execute:

bash
Copiar
Editar
python train_and_use_ai.py
Isso iniciará o treinamento com os dados de exemplo, realizará uma predição de teste e salvará (e recarregará) o modelo conforme definido.

Integração com Django (Opcional):
Se você deseja integrar o treinamento ao ambiente Django, pode transformar esse script em um comando customizado (como mencionado anteriormente) e rodá-lo com:

bash
Copiar
Editar
python manage.py train_bot