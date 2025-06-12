# AgentSupportAI

Agente IA para suporte técnico especializado em Produtos Digitais, utilizando processamento de linguagem natural e busca semântica em documentos internos.

## Tecnologias Utilizadas
- Python 3.11+
- [LangChain](https://python.langchain.com/)
- [LangChain Community](https://github.com/langchain-ai/langchain)
- [LangChain OpenAI](https://github.com/langchain-ai/langchain)
- [OpenAI API](https://platform.openai.com/)
- [FAISS](https://github.com/facebookresearch/faiss) (indexação vetorial)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [tiktoken](https://github.com/openai/tiktoken)
- [PyPDF](https://github.com/py-pdf/pypdf)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [unstructured](https://github.com/Unstructured-IO/unstructured) (para leitura de arquivos)
- [markdown](https://pypi.org/project/Markdown/) (para leitura de arquivos .md)

## Instalação

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd AgentSupportAI
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # ou
   source .venv/bin/activate  # Linux/Mac
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   pip install "unstructured>=0.4.16"
   pip install markdown
   ```
4. Configure sua chave da OpenAI:
   - Crie um arquivo `.env` na raiz do projeto com o conteúdo:
     ```env
     OPENAI_API_KEY=sua-chave-aqui
     ```

## Como usar

1. Coloque seus documentos em `/data` (suporta `.pdf`, `.md`, `.txt`).
2. Execute o script principal do agente:
   ```bash
   python main_agent.py
   ```
3. O sistema irá carregar o índice FAISS (ou criar um novo se não existir) e responder perguntas com base no conteúdo dos documentos.
   - Sempre que alterar arquivos em `/data`, apague a pasta `faiss_index` para forçar a reindexação automática.
   - O agente permite perguntas interativas no terminal. Digite `sair` para encerrar.

## Estrutura do Projeto
- `main_agent.py`: Script principal do agente, com reindexação automática e interação via terminal.
- `agents/agent.py`: Implementação do agente de perguntas e respostas.
- `agents/loader.py`: Carregamento e split de documentos.
- `agents/vectorstore.py`: Criação e carregamento do índice vetorial FAISS.
- `data/`: Pasta para documentos internos (suporta `.pdf`, `.md`, `.txt`).
- `faiss_index/`: Índice vetorial persistido (pode ser apagado para reindexação).
- `requirements.txt`: Dependências do projeto.

## Observações
- O projeto utiliza embeddings da OpenAI, portanto é necessário saldo na conta OpenAI.
- Para evitar problemas de depreciação, todas as dependências estão atualizadas.
- O índice FAISS é recriado automaticamente se não existir ou estiver vazio.
- Para atualizar o conhecimento do agente após mudanças em `/data`, basta apagar a pasta `faiss_index` antes de rodar.

---

> Projeto para automação de suporte interno e onboarding de colaboradores.