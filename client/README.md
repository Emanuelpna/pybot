# Chatbot Client

## Como rodar

Para rodar em modo de desenvolvimento, execute o comando abaixo e acesse o app em <http://localhost:5173/>

```bash
npm run dev
```

Para rodar em movo de produção, execute o comando abaixo e acesse o app em <http://localhost:4173/>

```bash
npm run build && npm run preview
```

# Chatbot de Curiosidades de Python

Este projeto é um chatbot educacional desenvolvido com o objetivo de auxiliar iniciantes na área de programação a aprender conceitos básicos da linguagem Python de forma interativa e divertida.

## Tema

Escolhemos como tema "Curiosidades de Python" por estarmos inseridos na área de TI e acreditarmos que seria uma forma interessante de reforçar e compartilhar o conhecimento com quem está começando.

## Tecnologias Utilizadas

- **Frontend:** React (JavaScript)
- **Backend:** FastAPI (Python)
- **NLP:** NLTK (Natural Language Toolkit)
- **Bibliotecas adicionais:** PyPDF2 (não usada diretamente na versão final, mas testada em protótipos)

## Estrutura do Projeto

- `client/` – Interface web do chatbot (React)
- `server/` – API que processa as mensagens usando NLTK
- `chat.html` – Template da interface de chat (renderizado pelo FastAPI)
- `pares` – Conjunto de padrões de perguntas/respostas (intents)
- `custom_reflections` – Refletores para tornar a conversa mais natural

## Estrutura do Diálogo

O chatbot funciona a partir de um conjunto de **expressões regulares (regex)** que identificam intenções do usuário e retornam respostas pré-definidas. Os pares são separados em:

- Perguntas gerais de boas-vindas
- Perguntas sobre sintaxe e conceitos básicos de Python

Exemplo:
```python
[ r"Como usar o for em Python", ["Exemplo: for i in range(5): print(i)"] ]

## Testes realizados
O chatbot foi testado manualmente pelos integrantes do grupo: Emanuel Andrade, Mayara Mikaelly e Urias Góes

Testes focaram em:

Correspondência correta das perguntas

Respostas coerentes

Comunicação fluida entre o frontend e o backend

Responsividade da interface

## Interface Web
Desenvolvida em React

Interface simples, limpa e responsiva

Ainda sem recursos de acessibilidade implementados

## Organização do Código
O projeto está organizado em duas pastas principais:
📁 client/
 └── src/
     └── components/
         └── Chat.js

📁 server/
 └── main.py (FastAPI + NLTK Chatbot)

Este projeto foi desenvolvido como atividade da disciplina Inteligência Artificial e Machine Learning (IAML), com foco em aplicar conceitos de NLP na prática.

