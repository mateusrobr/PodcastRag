from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer
collection_name = "video_subs"

def initialize_database(url="http://localhost:6333"):
    client = QdrantClient()
    encoder = SentenceTransformer("all-MiniLM-L6-v2")
    try:
        client.create_collection(
        collection_name=collection_name,
        vectors_config=models.VectorParams(
            size=encoder.get_sentence_embedding_dimension(),  # Vector size is defined by used model
            distance=models.Distance.COSINE,
    ),
)
        print(f"Coleção '{collection_name}' criada com sucesso.")
    except Exception as e:
        print(f"Coleção '{collection_name}' já existe. Ignorando criação. Erro: {e}")

    return client

def add_to_collection(doc, client):
    encoder = SentenceTransformer("all-MiniLM-L6-v2")
    client.upload_points(
        collection_name=collection_name,
        points=[
            models.PointStruct(
                id=1, vector=encoder.encode(doc["srt_subtitle"]).tolist(), payload=doc
            )
        ],
    )   

