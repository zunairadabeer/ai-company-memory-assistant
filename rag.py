from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def split_text(text, chunk_size=80):

    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


def search_relevant_chunks(question, documents, top_k=3):

    chunks = []

    for doc_id, title, content in documents:

        text_chunks = split_text(content)

        for chunk in text_chunks:
            chunks.append(
                {
                    "document_id": doc_id,
                    "title": title,
                    "content": chunk
                }
            )

    if len(chunks) == 0:
        return []

    chunk_texts = []

    for chunk in chunks:
        chunk_texts.append(chunk["content"])

    chunk_texts.append(question)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(chunk_texts)

    question_vector = vectors[-1]
    document_vectors = vectors[:-1]

    scores = cosine_similarity(
        question_vector,
        document_vectors
    )[0]

    ranked_results = sorted(
        zip(chunks, scores),
        key=lambda item: item[1],
        reverse=True
    )

    return ranked_results[:top_k]


def generate_answer(question, results):

    if len(results) == 0:
        return "I could not find anything relevant in the company memory yet."

    answer = "Relevant company memory found:\n\n"

    for item in results:

        chunk = item[0]
        score = item[1]

        answer += f"Source: {chunk['title']}\n"
        answer += f"Relevance score: {round(float(score), 3)}\n"
        answer += f"{chunk['content']}\n\n"

    answer += "This answer is based on the stored company memory above."

    return answer
