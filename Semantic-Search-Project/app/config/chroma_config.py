import chromadb

from app.config.settings import (
    CHROMA_STORAGE_PATH,
    COLLECTION_NAME
)

# Create a persistent ChromaDB client.
# All vectors and metadata will be stored inside the configured storage path.
client = chromadb.PersistentClient(
    path=CHROMA_STORAGE_PATH
)

# Get the collection if it already exists.
# Otherwise, create a new collection with the given name.
# A collection in ChromaDB is similar to a table in a relational database.
collection = client.get_or_create_collection(
    name=COLLECTION_NAME
)