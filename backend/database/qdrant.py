from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

client = QdrantClient(":memory:")

COLLECTION_NAME = "documents"

try:
    client.get_collection(COLLECTION_NAME)
except:
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config={
            "size": 384,
            "distance": "Cosine"
        }
    )


point_id = 0


def store_vector(
    chunk,
    embedding
):

    global point_id

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            PointStruct(
                id=point_id,
                vector=embedding,
                payload={
                    "chunk": chunk
                }
            )
        ]
    )

    point_id += 1


def search_vectors(
    embedding,
    limit=3
):

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=embedding,
        limit=limit
    )

    return results.points