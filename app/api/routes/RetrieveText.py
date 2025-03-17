from fastapi import APIRouter, HTTPException
from app.schemas.response import EmbeddingResponseSchema
from app.schemas.request import TextRequestSchema

router = APIRouter()

@router.get("/embed", response_model = EmbeddingResponseSchema)
async def retrieve_text(request: TextRequestSchema):
    try:
        embedding = retriever.obtain_similar_text(request.text)
        return { "text": request.text, "embedding": embedding }
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))