# vector.py
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv("amazon_reviews.csv")

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./amazon_chroma_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []
    
    for i, row in df.iterrows():
        content = f"{row['Summary']} {row['Text']}"
        metadata = {
            "score": row.get("Score", ""),
            "product_id": row.get("ProductId", ""),
            "time": row.get("Time", "")
        }
        document = Document(
            page_content=content,
            metadata=metadata,
            id=str(i)
        )
        documents.append(document)
        ids.append(str(i))

vector_store = Chroma(
    collection_name="amazon_reviews",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)

retriever = vector_store.as_retriever(search_kwargs={"k": 5})
