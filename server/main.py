from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from chatbot import chatbot
from infra.rag.llm_agent_creator import LLMAgentCreator
from infra.translator.translator import translate_google

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

llm, retriever, query_prompt = LLMAgentCreator.bind()


@app.get('/')
def read_root():
    return {'message': 'PyBot'}


@app.get('/chat_old')
def read_root(user_message: str):
    response = chatbot.respond(user_message)
    return {'message': response}


@app.get('/chat')
def read_root(user_message: str):
    print("Translating user message to English with Google Translate")
    translated_to_english_user_message = translate_google(user_message, 'en')
    print("   -> Finished")

    print("Retrieving documents relevant to the question on the python docs")
    relevant_docs = retriever.invoke({"question": translated_to_english_user_message, "relevant_docs": []}, verbose=True)
    print("   -> Finished")

    print("Asking the chatbot")
    response = llm.invoke({"question": translated_to_english_user_message, "relevant_docs": relevant_docs[:5]})
    print("   -> Finished")

    return {"message": response}
