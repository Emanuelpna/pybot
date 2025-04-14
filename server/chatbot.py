import random
from http.client import responses

import nltk
from nltk.chat.util import Chat, reflections

pares = [
    (
        r"oi|olá|e aí|opa",
        ["Olá!", "Como posso ajudar você?", "Oi, como está?"]
    ),
    (
        r"qual é o seu nome\?",
        ["Meu nome é ChatBot NLTK.", "Você pode me chamar de ChatBot NLTK.", "Sou o ChatBot NLTK."]
    ),
    (
        r"meu nome é (.*)",
        ["Olá, %1. Prazer em te conhecer!"]
    ),
    (
        r"(.*)\?",
        ["Desculpe, não tenho uma resposta específica para essa pergunta.", "Pode reformular a pergunta?"]
    )
]

pares.extend([
    (
        r"(.*)",
        ["Entendi, diga-me mais.", "Pode me contar mais sobre isso?", "Interessante. Conte-me mais."]
    )
])

reflections = {
    "eu": "você",
    "meu": "seu",
    "meus": "seus",
    "minha": "sua",
    "minhas": "suas",
    "sou": "é",
    "estou": "está",
    "fui": "foi",
    "era": "foi",
    "você": "eu",
    "você é": "eu sou",
    "você está": "eu estou"
}

chatbot = Chat(pares, reflections)

def iniciar_chat():
    print('Bem-vindo ao ChatBot NLTK! Digite "sair" para encerrar.')
    while True:
        user_input = input("Você: ")

        if user_input.lower() == 'sair':
            print("ChatBot: Adeus!")
            break

        response = chatbot.respond(user_input)
        print("ChatBot: ", response)
