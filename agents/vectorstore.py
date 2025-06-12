from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import os


def create_vector_store(chunks, persist_path='faiss_index'):
    """
  Cria um repositório de vetores FAISS a partir dos blocos de texto fornecidos.

    Argumentos:
    chunks (lista): Lista de blocos de texto a serem indexados.
    persist_path (str): Caminho para persistir o índice FAISS.

    Retorna:
    FAISS: Uma instância do repositório de vetores FAISS.
    """
    # instancia o modelo de embeddings
    embeddings = OpenAIEmbeddings()

    # cria o indice FAISS  a parti dos chunks vetorizados
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # salva localmente
    vectorstore.save_local(persist_path)

    return vectorstore

def load_vector_store(persist_path='faiss_index'):
    embendings = OpenAIEmbeddings()
    return FAISS.load_local(persist_path, embendings, allow_dangerous_deserialization=True)
