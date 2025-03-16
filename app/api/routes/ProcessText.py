from fastapi import APIRouter, HTTPException

from app.schemas.request import TextRequest
from app.schemas.response import EmbeddingResponse

from app.services.indexer import text_to_embedding
from app.services.retriever import retriever

router = APIRouter()

@router.get("/chat")
async def read_chat():
    # Simulates the chat landing page.
    return {"Message": "This is the chat endpoint."}

@router.post("/embed", response_model = embedding_model)
async def embed_text(request: TextRequest):
    try:
        embedding = text_to_embedding(request.text)
        retriever.add_text(request.text)
        return {"text": request.text, "embedding": embedding}
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))
