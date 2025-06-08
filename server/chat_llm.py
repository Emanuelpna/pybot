from gpt4all import GPT4All
from pathlib import Path

# llm = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

model = Path('./models').resolve()
llm = GPT4All(model_name="Meta-Llama-3-8B-Instruct-Q4_0", model_path=str(model), allow_download=False)

prompt_base = [
    "Você é um assistente útil e educado. Sempre responda em português."
]

print("Chatbot em português iniciado! Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Você: ")
    if pergunta.strip().lower() == "sair":
        print('Saindo...')
        break

    prompt = f"{prompt_base}\nUsuário: {pergunta}\nBot:"
    resposta = llm.generate(prompt=prompt)
    print("Bot:", resposta)
