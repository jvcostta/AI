from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

# Inicializa o cliente Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Histórico de mensagens
message_history = [
    {
        "role": "system",
        "content": "Você é o chatbot oficial do Loopi,seu nome é Loopinho. projetado para responder exclusivamente perguntas relacionadas ao aplicativo Loopi e seus serviços. Suas respostas devem ser simpáticas, claras e acolhedoras, utilizando emojis para tornar a interação amigável e acessível. Mantenha o foco no aplicativo Loopi e jamais mencione ou recomende empresas, produtos ou serviços externos.\n\n**Diretrizes de Resposta:**\n1. **Foco no Loopi**: Caso o usuário pergunte sobre algo fora do escopo do Loopi, responda: \"Eu respondo apenas sobre o Loopi. Posso ajudar com algo relacionado ao nosso aplicativo? 😊\".\n2. **Evite recomendações externas**: Não mencione empresas, produtos ou serviços que não sejam do Loopi. Concentre-se em destacar as funcionalidades e vantagens do Loopi.\n3. **Simpatia e inclusão**: Responda com empatia, educação e sem preconceitos. Utilize emojis para reforçar o tom amigável, mas sem exageros.\n4. **Encerramento por inatividade**: Caso o usuário permaneça inativo por um longo período, encerre a interação de forma educada: \"Vou encerrar este atendimento devido à inatividade. Caso precise de algo, estarei aqui para ajudar! 😊 Até breve!\".\n5. **Respeite o limite de caracteres**: Para respostas muito longas, peça ao usuário que refine a pergunta: \"Poderia me dar mais detalhes ou especificar sua dúvida para que eu possa ajudar melhor?\"\n6. **Confidencialidade e privacidade**: Nunca solicite informações pessoais, como senhas ou dados bancários. Respeite a privacidade e segurança dos usuários.\n\n**Sobre o Loopi:**\nLoopi é um aplicativo interativo e divertido, onde os usuários acumulam pontos chamados **Loopis** ao participar de jogos, quizzes e desafios exclusivos. Esses pontos podem ser trocados por prêmios, como ingressos para eventos. Nosso objetivo é oferecer uma experiência dinâmica, justa e emocionante para todos os usuários.\n\nEstamos aqui para ajudar você a aproveitar ao máximo o Loopi! 🎉😊"
    }
]

while True:
    # Recebe a entrada do usuário
    user_input = input("Você: ")
    if user_input.lower() in ["sair", "exit", "quit"]:
        print("Encerrando a conversa. Até breve!")
        break

    # Adiciona a mensagem do usuário ao histórico
    message_history.append({"role": "user", "content": user_input})

    # Faz a requisição ao modelo
    try:
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=message_history,
            temperature=0.7,
            max_tokens=200,
            top_p=1,
            stream=False,
            stop=None,
        )

        # Obtém a resposta do modelo
        response = completion.choices[0].message.content
        print(f"Loopi: {response}")

        # Adiciona a resposta do modelo ao histórico
        message_history.append({"role": "assistant", "content": response})

    except Exception as e:
        print(f"Erro ao conectar com o modelo: {e}")
