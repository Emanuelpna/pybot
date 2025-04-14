# Chatbot Server

## Como rodar

Crie um ambiente virtual para o python

```bash
python -m venv .venv
```

Ative o ambiente com um dos comandos abaixo de acordo com seu sistema operacional

```bash
source ./.venv/bin/activate # linux 
```

```bash
./.venv/Scripts/Activate.ps1 # windows 
```

Instale as dependências do projeto

```bash
pip install -r requirements.txt
```

Baixe os pacotes do `nltk`

```bash
python -m nltk.downloader all
```

Execute a API do FastApi:

```bash
fastapi dev main.py
```