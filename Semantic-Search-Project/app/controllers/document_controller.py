# app/api/search.py

from fastapi import APIRouter
from app.services.document_service import search

router = APIRouter()

@router.get("/search")
def search_api(query: str):
    return {
        "query": query,
        "results": search(query)
    }