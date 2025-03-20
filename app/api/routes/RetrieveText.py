from fastapi import APIRouter, HTTPException
from app.schemas.response import EmbeddingResponseSchema
from app.schemas.request import TextRequestSchema
'''from app.services.retriever import similarity_search

router = APIRouter()

@router.get("/retrieve", response_model = EmbeddingResponseSchema)
async def retrieve_text(request: TextRequestSchema):
    try:
        embedding = similarity_search(request.text)
        return { "text": request.text, "embedding": embedding }
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))'''

