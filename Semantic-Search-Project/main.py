from fastapi import FastAPI
from app.controllers.document_controller import router as document_controller

# Create FastAPI app
app = FastAPI()

print("Welcome to semantic search project !!")

# Include routes from controller (router)
app.include_router(document_controller)


# Optional root endpoint
# @app.get("/")
# def root():
#     return {"message": "Semantic Search API is running"}