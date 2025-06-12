from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

def create_agent(vectorstore, llm=None):
    llm = ChatOpenAI(temperature=0)
    agente = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )
    return agente
