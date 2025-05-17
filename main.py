from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

# Process PDF and return vector DB
def process_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    

    vectordb = Chroma.from_documents(docs, embedding=embeddings, persist_directory="./chroma_db")
    vectordb.persist()

    return vectordb

# Generate answer using RAG
def generate_answer(vectordb, user_query):
   # llm = Ollama(model="mistral")  # You can change model name
   # qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())



    llm = Ollama(model="mistral:latest")

    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectordb.as_retriever())

    return qa_chain.run(user_query)
