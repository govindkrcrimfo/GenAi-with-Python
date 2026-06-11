from sentence_transformers import SentenceTransformer
import chromadb
import uuid

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_storage")

# Get collection
# collection = client.get_collection("jobs_collection")
def get_collection():
    return client.get_collection("jobs_collection")

def search(query: str, n_results: int = 2):
    """
    Search similar documents from ChromaDB
    """

    collection = get_collection()  # 🔥 fresh reference

    # Convert user query into embedding
    query_embedding = model.encode(query).tolist()

    # Search similar documents
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    return results["documents"][0]

def add_document(text: str):
    """
    Add a new document to ChromaDB
    """
    collection = get_collection()  # 🔥 fresh reference

    # Generate embedding for the document text
    embedding = model.encode(text).tolist()

    document_id = str(uuid.uuid4())
    # Store document, embedding and ID in ChromaDB
    collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[document_id]
    )
    return {
        "message": "Document added successfully",
        "document_id": document_id
    }
