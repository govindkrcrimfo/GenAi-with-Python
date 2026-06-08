from sentence_transformers import SentenceTransformer  # Import embedding model

model = SentenceTransformer("all-MiniLM-L6-v2")  # Load pre-trained transformer model

text = "Hello semantic search"

embedding = model.encode(text)  # Convert text → vector (embedding)

print(len(embedding))  # Check embedding size (usually 384)
print(embedding[:5])  # Print first 5 values of vector