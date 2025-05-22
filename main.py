from fastapi import FastAPI
from pydantic import BaseModel
from qa_chain import get_answer  # تأكد إن هاد الملف والتابع موجودين عندك

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def root():
    return {"message": "Server is running!"}

@app.post("/ask")
def ask_question(request: QuestionRequest):
    answer = get_answer(request.question)
    return {"answer": answer}
