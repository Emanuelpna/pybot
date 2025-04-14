# PyBot

Para usar o projeto, é necessário iniciar ambas as aplicações web e de servidor.

Veja detalhes de [como rodar a aplicação web](client/README.md) e de [como rodar o servidor](server/README.md)

## Chatbot de Curiosidades de Python

Este projeto é um chatbot educacional desenvolvido com o objetivo de auxiliar iniciantes na área de programação a aprender conceitos básicos da linguagem Python de forma interativa e divertida.

### Tema

Escolhemos como tema "Curiosidades de Python" por estarmos inseridos na área de TI e acreditarmos que seria uma forma interessante de reforçar e compartilhar o conhecimento com quem está começando.

### Tecnologias Utilizadas

- **Frontend:** React (JavaScript)
- **Backend:** FastAPI (Python)
- **NLP:** NLTK (Natural Language Toolkit)

### Estrutura do Projeto

- `client/` – Interface web do chatbot (React)
- `server/` – API que processa as mensagens usando NLTK
- `pares` – Conjunto de padrões de perguntas/respostas (intents)
- `reflections` – Refletores para tornar a conversa mais natural

### Estrutura do Diálogo

O chatbot funciona a partir de um conjunto de **expressões regulares (regex)** que identificam intenções do usuário e retornam respostas pré-definidas. Os pares são separados em:

- Perguntas gerais de boas-vindas
- Perguntas sobre sintaxe e conceitos básicos de Python

Exemplo:

```python
( r"Como usar o for em Python", ["Exemplo: for i in range(5): print(i)"] )
```

### Testes realizados

O chatbot foi testado manualmente pelos integrantes do grupo: Emanuel Andrade, Mayara Mikaelly e Urias Góes

Testes focaram em:

Correspondência correta das perguntas

Respostas coerentes

Comunicação fluida entre o frontend e o backend

Responsividade da interface

### Interface Web

Desenvolvida em React

Interface simples, limpa e responsiva
