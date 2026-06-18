import sqlite3

DB_NAME = "company_memory.db"


def create_tables():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_document(title, content):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO documents (title, content) VALUES (?, ?)",
        (title, content)
    )

    conn.commit()
    conn.close()


def get_all_documents():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, title, content FROM documents"
    )

    documents = cursor.fetchall()

    conn.close()

    return documents
