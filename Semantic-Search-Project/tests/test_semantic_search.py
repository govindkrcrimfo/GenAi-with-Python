from sentence_transformers import SentenceTransformer  # Import again (redundant but OK for test)
import chromadb  # Import ChromaDB again

model = SentenceTransformer("all-MiniLM-L6-v2")  # Load embedding model again

client = chromadb.PersistentClient(path="./chroma_storage")  # Connect to same DB folder
collection = client.get_or_create_collection("test_collection")  # Access same collection

docs = [
    "Java is a backend language",
    "Python is used for machine learning",
    "FastAPI builds APIs",
    "ChromaDB stores vectors"
]

embeddings = model.encode(docs).tolist()  # Convert all documents → embeddings (vector list)

collection.add(
    documents=docs,  # Store documents
    embeddings=embeddings,  # Store their vector representations
    ids=["1", "2", "3", "4"]  # Unique IDs (IMPORTANT: should not repeat in real apps)
)

query = "What is used for ML?"

query_embedding = model.encode(query).tolist()  # Convert query → vector

results = collection.query(
    query_embeddings=[query_embedding],  # Search nearest vectors
    n_results=2  # Return top 2 similar documents
)

print(results["documents"])  # Final semantic search output