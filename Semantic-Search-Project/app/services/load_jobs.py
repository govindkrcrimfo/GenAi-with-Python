from sentence_transformers import SentenceTransformer
import chromadb

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB storage
client = chromadb.PersistentClient(path="./chroma_storage")

# Create or get collection
collection = client.get_or_create_collection(
    name="jobs_collection"
)

# Read all lines from jobs.txt
with open("data/jobs.txt", "r") as file:
    jobs = [line.strip() for line in file if line.strip()]

# Generate embeddings for all jobs
embeddings = model.encode(jobs).tolist()

# Generate unique IDs
ids = [str(i) for i in range(len(jobs))]

# Store documents and embeddings in ChromaDB
collection.upsert(
    documents=jobs,
    embeddings=embeddings,
    ids=ids
)

print(f"{len(jobs)} records loaded successfully.")