import chromadb  # Import ChromaDB (vector database)

client = chromadb.PersistentClient(path="./chroma_storage")  # Create persistent DB storage

collection = client.get_or_create_collection("test_collection")  # Create or get collection

collection.add(
    documents=["Java is a language", "Python is for ML"],  # Text data stored in DB
    ids=["1", "2"]  # Unique IDs for each document
)

print("Inserted successfully")  # Confirm data insertion