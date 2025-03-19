from fastapi import APIRouter, HTTPException
from app.schemas.response import EmbeddingResponseSchema
from app.schemas.request import TextRequestSchema
from app.services.retriever import similarity_search

router = APIRouter()

@router.get("/scrape")
async def scrape_text(request: TextRequestSchema):
    try:
        text = scrape_website(request.text)
        return { "text": request.text, "embedding": embedding }
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))