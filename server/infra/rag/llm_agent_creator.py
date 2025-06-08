from pathlib import Path

from langchain_community.llms import GPT4All
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from infra.text_loader.text_loader import TextLoader
from infra.rag.line_list_output_parser import LineListOutputParser
from infra.filesystem.get_files_from_folder import get_files_from_folder
from infra.query_retriever.pybot_multi_query_retriever import PybotMultiQueryRetriever


class LLMAgentCreator:
    def __init__(self):
        self.documents = []
        self.vector_store = None

    @staticmethod
    def bind():
        llm_creator = LLMAgentCreator()

        files = get_files_from_folder("./resources/python_docs")
        # for file in files:
        #     print("Processing file: ", file)
        #     llm_creator.add_document(file)
        #     print("  -> File processing finished")
        llm_creator.add_document("installing.txt")

        llm_creator.create_vector_store()

        return llm_creator.get_chatbot()

    def add_document(self, filename):
        text_loader = TextLoader()

        documents = text_loader.process_document(filename)

        self.documents.append(documents)

    def create_vector_store(self):
        embeddings = HuggingFaceEmbeddings(
            model_name='ibm-granite/granite-embedding-278m-multilingual',
            model_kwargs={'device': 'cpu'}
        )

        documents_flatten = [
            element
            for sublist in self.documents
            for element in sublist
        ]

        print("Sending documents to vector store")
        self.vector_store = FAISS.from_documents(documents_flatten, embeddings)
        print("   -> Finished")

    def get_chatbot(self):
        if self.vector_store is None:
            self.create_vector_store()

        model = Path('./models/').resolve()
        llm = GPT4All(
            model=str(model) + "/Meta-Llama-3-8B-Instruct-Q4_0",
            allow_download=False,
            verbose=True
        )

        query_prompt = PromptTemplate(
            input_variables=["question", "relevant_docs"],
            template="""Your name is PyBot, you are a useful chatbot that answers questions about Python language only. 
            You don't need to explain you answers. 
            Only you speak with the user asking, don't tell about assistants or others persons. 
            Use markdown style syntax on your answers. 
            You always generate a short and useful answer only using brazilian portuguese to the question: {question} 
            Use the relevant documents below whenever possible\n\n{relevant_docs}"""
        )

        output_parser = LineListOutputParser()
        llm_chain = query_prompt | llm | output_parser

        print("Getting retriever with documents loaded")
        retriever = PybotMultiQueryRetriever(
            parser_key="lines",
            llm_chain=llm_chain,
            retriever=self.vector_store.as_retriever(),
        )
        print("   -> Finished")

        return llm_chain, retriever, query_prompt
