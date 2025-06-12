from langchain_community.document_loaders import PyPDFLoader, TextLoader, UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os


def load_documents(directory="./data"):
    documents = []

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if filename.endswith('.pdf'):
            loader = PyPDFLoader(filepath)
        elif filename.endswith('.md'):
            loader = UnstructuredMarkdownLoader(filepath)
        elif filename.endswith('.txt'):
            loader = TextLoader(filepath)
        else:
            print(f"formato não suportado: {filename}")
            continue
    
        docs = loader.load()
        documents.extend(docs)
    
    return documents

def split_documents(documents, chunk_size=500, chunk_overlap=100):
    if not documents:
        print("Nenhum documento recebido para dividir.")
        return []
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    return splitter.split_documents(documents)





     
