from sentence_transformers import SentenceTransformer
import chromadb

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_storage")

# Get collection
collection = client.get_collection("jobs_collection")


def search(query: str, n_results: int = 3):
    """
    Search similar documents from ChromaDB
    """

    # Convert user query into embedding
    query_embedding = model.encode(query).tolist()

    # Search similar documents
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results["documents"][0]