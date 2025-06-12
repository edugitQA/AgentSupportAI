from dotenv import load_dotenv
load_dotenv()

from agents.loader import load_documents, split_documents  # Adicionado para reindexação
from agents.vectorstore import load_vector_store, create_vector_store  # Adicionado para reindexação
from agents.agent import create_agent
import os

# Sempre que houver alteração nos arquivos da pasta data/, reindexe FAISS
# Para forçar a reindexação, delete o diretório faiss_index antes de rodar o agente
if not os.path.exists('faiss_index') or not os.listdir('faiss_index'):
    docs = load_documents("data")
    chunks = split_documents(docs)
    create_vector_store(chunks)
    # Comentário: Isso garante que o índice será criado se não existir ou se for apagado

vectorstore = load_vector_store()
agente = create_agent(vectorstore)

while True:
    query = input("\nDigite sua pergunta (ou 'sair' para encerrar): ")
    if query.strip().lower() == 'sair':
        print("Encerrando o agente.")
        break

    res = agente(query)

    print("\nResposta do agente:")
    print(res['result'])

    print("\nFontes usadas:")
    for doc in res['source_documents']:
        print("-", doc.metadata.get("source", "Fonte desconhecida"))