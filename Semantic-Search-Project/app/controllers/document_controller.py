# app/api/search.py

from fastapi import APIRouter
from app.services.document_service import search , add_document
from app.models.document import DocumentRequest
router = APIRouter()

@router.get("/search")
def search_api(query: str):
    return {
        "query": query,
        "results": search(query)
    }

@router.post("/addDocuments")
def add_document_api(document: DocumentRequest):
    return add_document(
        text=document.text
    )