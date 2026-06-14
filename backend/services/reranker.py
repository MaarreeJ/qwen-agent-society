from sentence_transformers import CrossEncoder

reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank_chunks(
    query,
    chunks,
    top_k=3
):

    pairs = [
        [query, chunk]
        for chunk in chunks
    ]

    scores = reranker.predict(
        pairs
    )

    ranked = sorted(
        zip(scores, chunks),
        reverse=True
    )

    return [
        chunk
        for score, chunk
        in ranked[:top_k]
    ]