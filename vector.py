from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

import os
from scraper import scrape_roma


def create_vector_store():

    # vector db klasoru
    db_location = "./roma_chroma_db"

    # if DB varsa tekrar scrape + embed yapma
    if os.path.exists(db_location):
        embeddings = OllamaEmbeddings(model="mxbai-embed-large")

        vector_store = Chroma(
            collection_name="roma_travel",
            persist_directory=db_location,
            embedding_function=embeddings
        )

        return vector_store

    # Roma icerigini scrape ettik
    text = scrape_roma()

    # document formatina cevirdik
    docs = [Document(page_content=text)]

    # chunking islemi
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    # embedding modeli
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")

    # vector store olusturduk
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name="roma_travel",
        persist_directory=db_location
    )

    return vector_store


# retriever olusturma fonksiyonu
def get_retriever():
    vector_store = create_vector_store()

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever

