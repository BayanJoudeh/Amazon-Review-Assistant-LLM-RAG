# Amazon Review Assistant LLM + RAG

**Amazon Review Assistant** is an AI-powered tool designed to help users quickly find answers from thousands of Amazon product reviews using Retrieval Augmented Generation (RAG) and Large Language Models (LLM).

## Project Overview

The system includes three main parts:

- **Vector Database**: Uses Chroma and Ollama embeddings to store and search Amazon review vectors.  
- **Backend API**: Built with FastAPI, processes questions and returns AI-generated answers.  
- **Frontend Interface**: Developed with Streamlit, offering a user-friendly UI with a baby blue theme.

## Features

- Semantic search across extensive Amazon reviews  
- Natural language Q&A about products and customer feedback  
- Concise, product-specific insights  
- Privacy-focused: no data or questions stored  
- Clean, responsive UI  

## Live Demo

You can try the application live here:
[https://amazon-review-assistant-llm-rag-nyab7vrpgc7zxmedgbsahy.streamlit.app/](https://amazon-review-assistant-llm-rag-nyab7vrpgc7zxmedgbsahy.streamlit.app/)

*(Note: The performance and availability of the live demo depend on the hosting resources.)*

## Setup Instructions

### Prerequisites
- Python 3.8+  
- Ollama (for local LLM)  
- Git  

### Installation
```bash
git clone https://github.com/yourusername/amazon-review-assistant.git
cd amazon-review-assistant
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

```
### Data Preparation

Download the Amazon reviews dataset and place it in the project root:  
`amazon_reviews.csv` (contains ProductId, Score, Summary, Text, Time, etc.)

**Dataset Link:** [https://www.kaggle.com/datasets/arhamrumi/amazon-product-reviews?utm_source=chatgpt.com]

## Running the Application

Download required Ollama models:

```bash
ollama pull mxbai-embed-large
ollama pull llama3:instruct

```
Start the FastAPI backend server:
```bash
uvicorn main:app --host 0.0.0.0 --port 8002
```

In a new terminal, start the Streamlit frontend:
```bash
streamlit run app.py
```
Open your browser and navigate to: `http://localhost:8501`

## Screenshots

**Main Interface:**
![stramlitt](https://github.com/user-attachments/assets/990e1f5b-0f15-4ab6-a09c-c3bd20d7ec10)

**Example Interaction:**

![streamlit2](https://github.com/user-attachments/assets/33f52bad-617e-4805-8612-62ec51bed6a4)



*Screenshots showing the Amazon Review Assistant frontend interface and an example of the AI providing an answer.*

