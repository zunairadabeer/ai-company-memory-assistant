# AI Company Memory Assistant

Made this project to learn a bit more about how retrieval systems work. The program stores company documents and lets users ask questions about them. It then searches for the most relevant information and returns it.

## Built With

- Python
- FastAPI
- SQLite
- Scikit-Learn

## How It Works

1. Add documents to the database
2. Split documents into chunks
3. Convert text into vectors using TF-IDF
4. Compare similarity scores
5. Return the most relevant chunks

## Running the Project

Install the requirements:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn main:app --reload
```

## Things I'd Like To Add

- Better search accuracy
- Vector embeddings
- Frontend UI
- User accounts

This was mainly a learning project to get some experience with FastAPI, databases and information retrieval.
