from sentence_transformers import SentenceTransformer

from app.config.settings import EMBEDDING_MODEL_NAME

# Load the embedding model at application startup.
# This model converts text into numerical vectors (embeddings)
# that are used for semantic similarity search.
model = SentenceTransformer(
    EMBEDDING_MODEL_NAME
)