import nltk
from nltk.chat.util import Chat

pares = [
    (r"Oi|Ol(á|a)|E aí", ["Olá!", "Como posso ajudar você com Python?", "Oi! Preparado para aprender Python?"]),
    (r"Qual o seu nome\??",
     ["Me chame de PyBot!", "Sou o PyBot, seu ajudante de Python!", "Sou seu assistente de estudos!"]),
    (r"Qual (é|e) o seu prop(ó|o)sito\??",
     ["Estou aqui para te ajudar a aprender Python!", "Meu propósito é ensinar programação com Python."]),
    (r"Como você (está|esta)\??", ["Estou pronto para programar com você!", "100% funcional e pronto para responder."]),
    (r"adeus|tchau", ["Tchau! Bons estudos com Python!", "Até logo, continue praticando Python!"]),
    (r".*meu nome (é|e) (.*)", ["Olá %1, vamos aprender Python juntos!"]),
]

pares.extend([
    (r"O que (é|e) Python\??", ["Python é uma linguagem de programação de alto nível, fácil de aprender e muito versátil."]),
    (r"(para|pra) que serve o Python\??",
     ["Python é usado para desenvolvimento web, análise de dados, automação, IA e muito mais."]),
    (r"Como declarar uma vari(á|a)vel em Python\??", ["Basta usar um nome e atribuir um valor. Ex: idade = 25"]),
    (r"O que (é|e) um loop\??", ["Um loop é uma estrutura que repete um bloco de código."]),
    (r"Como usar o for em Python\??", ["Exemplo: for i in range(5): print(i)"]),
    (r"Como usar o while em Python\??", ["Exemplo: while x < 10: print(x); x += 1"]),
    (r"Como criar uma fun(çã|ca)o em Python\??", ["Use 'def'. Exemplo: def minha_funcao(): print('Olá')"]),
    (r"Para que serve o if\??", ["'if' é usado para criar condições. Exemplo: if x > 10: print('Maior que 10')"]),
    (r"Como comentar um c(ó|o)digo\??", ["Use # para comentários de linha única."]),
    (r"O que (é|e) uma lista\??", ["Lista é uma coleção ordenada. Exemplo: numeros = [1, 2, 3]"]),
    (r"Como acessar um item da lista\??", ["Use o índice. Ex: numeros[0] retorna o primeiro item."]),
    (r"Como adicionar um item na lista\??", ["Use append(). Exemplo: lista.append('novo item')"]),
    (r"Como remover um item da lista\??", ["Use remove(). Ex: lista.remove('valor')"]),
    (r"Como ordenar uma lista\??", ["Use sort(). Ex: lista.sort()"]),
    (r"Como criar um dicion(á|a)rio\??", ["Exemplo: pessoa = {'nome': 'Ana', 'idade': 20}"]),
    (r"Como acessar um valor no dicion(á|a)rio\??", ["Use a chave. Ex: pessoa['nome']"]),
    (r"O que (é|e) None\??", ["None representa a ausência de valor em Python."]),
    (r"O que (é|e) uma string\??", ["Uma string é uma sequência de caracteres. Ex: 'Olá mundo'"]),
    (r"Como converter string em inteiro\??", ["Use int(). Exemplo: int('10')"]),
    (r"Como imprimir no console\??", ["Use print(). Exemplo: print('Olá')"]),
])

pares.extend([
    (r"(.*)\??", ["Hmm, não entendi bem. Pode reformular?", "Boa pergunta! Mas preciso que você explique melhor."]),
    (r"(.*)", ["Entendi, diga-me mais.", "Pode me contar mais sobre isso?", "Interessante. Conte-me mais."])
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
    "você está": "eu estou",
}

chatbot = Chat(pares, reflections)

def iniciar_chat():
    print('Bem-vindo ao PyBot! Digite "sair" para encerrar.')
    while True:
        user_input = input("Você: ")

        if user_input.lower() == 'sair':
            print("ChatBot: Adeus!")
            break

        response = chatbot.respond(user_input)
        print("ChatBot: ", response)
