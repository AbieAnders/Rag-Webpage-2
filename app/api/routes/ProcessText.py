from fastapi import APIRouter, HTTPException
from app.schemas.request import TextRequestSchema
from app.schemas.response import EmbeddingResponseSchema
from app.services.embedder import text_to_embedding

router = APIRouter()

@router.post("/embed", response_model = EmbeddingResponseSchema)
async def embed_text(request: TextRequestSchema):
    try:
        embedding = text_to_embedding(request.text)
        return {"text": request.text, "embedding": embedding}
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))