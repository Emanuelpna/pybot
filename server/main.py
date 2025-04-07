from chatbot import chatbot

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
    return {'message': 'Chatbot NLTK'}

@app.get('/chat')
def read_root(user_message: str):
    response = chatbot.respond(user_message)
    return {'message': response}
