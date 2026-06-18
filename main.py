from fastapi import FastAPI
from pydantic import BaseModel

from database import create_tables
from database import add_document
from database import get_all_documents

from rag import search_relevant_chunks
from rag import generate_answer

app = FastAPI(
    title="AI Company Memory Assistant"
)

# create database tables when app starts
create_tables()


class DocumentInput(BaseModel):
    title: str
    content: str


class QuestionInput(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "AI Company Memory Assistant Running",
        "status": "online"
    }


@app.post("/add-document")
def upload_document(document: DocumentInput):

    add_document(
        document.title,
        document.content
    )

    return {
        "message": "Document uploaded successfully",
        "title": document.title
    }


@app.get("/documents")
def view_documents():

    documents = get_all_documents()

    document_list = []

    for doc in documents:

        document_list.append(
            {
                "id": doc[0],
                "title": doc[1],
                "preview": doc[2][:100]
            }
        )

    return {
        "total_documents": len(documents),
        "documents": document_list
    }


@app.post("/ask")
def ask_question(data: QuestionInput):

    # load all stored documents
    documents = get_all_documents()

    # retrieve the most relevant chunks
    results = search_relevant_chunks(
        data.question,
        documents
    )

    answer = generate_answer(
        data.question,
        results
    )

    sources = []

    for item in results:

        chunk = item[0]
        similarity = item[1]

        sources.append(
            {
                "title": chunk["title"],
                "score": round(float(similarity), 3)
            }
        )

    return {
        "question": data.question,
        "answer": answer,
        "sources": sources
    }
