from langchain_community.document_loaders import TextLoader as LangChainTextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

class TextLoader:
    def __init__(self, document_path='resources/python_docs/'):
        self.document_path = document_path

    def process_document(self, filename: str):
        document_loader = LangChainTextLoader(self.document_path + filename)
        document_loaded = document_loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=64)

        documents = text_splitter.split_documents(document_loaded)

        return documents