from database.qdrant import search_vectors
from services.embedding_service import create_embedding
from services.reranker import rerank_chunks


def retrieve_relevant_chunks(
    query: str,
    top_k: int = 3
):

    query_embedding = create_embedding(query)

    results = search_vectors(
        query_embedding,
        limit=10
    )

    chunks = []

    for item in results:

        chunks.append(
            item.payload["chunk"]
        )

    return rerank_chunks(
        query,
        chunks,
        top_k=3
    )