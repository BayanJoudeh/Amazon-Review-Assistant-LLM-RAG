from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3:instruct")

template = """
You are an expert in answering questions about Amazon product reviews.

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def get_answer(question: str) -> str:
    docs = retriever.get_relevant_documents(question)
    
    reviews_text = "\n\n".join([doc.page_content for doc in docs])
    
    return chain.invoke({"reviews": reviews_text, "question": question})
