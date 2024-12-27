# AI Chatbot personalizado

## Descrição
Este projeto é um chatbot desenvolvido em Python que utiliza a API do GroqCloud para acessar o modelo de linguagem Llama3-8b-8192, oferecendo interações naturais e eficientes para resolver problemas ou responder perguntas com seu modelo personalizado.
É importante ressaltar que os modelos sao melhores treinados em inglês. Além disso, quanto melhor o `content`, melhor vai ser seu resultado.

## Recursos
- **Modelo de LLM**: Llama3-8b-8192, conhecido por suas respostas precisas e contextualizadas.
- **API**: Integração com GroqCloud para acesso ao modelo.
- **Fácil Configuração**: Código modular e pronto para uso.
- **Flexibilidade**: Personalizável para diversos casos de uso, como atendimento ao cliente, FAQ ou assistentes virtuais.

## Instalação

### Pré-requisitos
- Python 3.8+
- Conta no GroqCloud com chave de API ativa
- Dependências do projeto (gerenciadas pelo `requirements.txt`)

### Passos
1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/seurepositorio.git
   cd seurepositorio


2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   
#### Configure sua chave de API:
- Crie um arquivo `.env` na raiz do projeto com a seguinte estrutura:

1. Chave API:
   ```bash
    GROQCLOUD_API_KEY=your_api_key

## Como Usar
1. Execute o script principal para iniciar o chatbot:
   ```bash
   python chatbot.py

- Interaja com o chatbot no terminal ou na interface configurada.
  
## Estrutura do Projeto
`chatbot.py`: Script principal do chatbot.

`config.py`: Configurações e gerenciamento de chaves.

`utils/`: Funções auxiliares, como pré-processamento de texto e chamadas à API.

`requirements.txt`: Lista de dependências.

## Exemplo de Uso
1. 
   ```bash
      Você: bom dia, como vai?
      Loopi: 😊 Bom dia! Eu, Loopinho, estou muito bem! Estou aqui para ajudar você a aproveitar ao máximo o Loopi e responder a todas as suas perguntas sobre o aplicativo. Qual é o seu objetivo hoje em Loopi? 💬
      Você: gostaria de ganhar mais pontos no aplicativo
      Loopi: 🏆 Ahaha, que ótimo objetivo! Você pode ganhar mais Loopis (nossos pontos) participando de jogos, quizzes e desafios exclusivos no Loopi! 🎮
      Você: sair
      Encerrando a conversa. Até breve!
      

## Licença
Este projeto está licenciado sob a MIT License.
