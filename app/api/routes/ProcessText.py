from fastapi import APIRouter, HTTPException

from app.schemas.request import TextRequestSchema
from app.schemas.response import EmbeddingResponseSchema

from app.services.embedder import text_to_embedding
#from app.services.upserter import update_or_insert
#from app.services.retriever import retriever

router = APIRouter()

@router.get("/chat")
async def read_chat():
    # Simulates the chat landing page.
    return {"Message": "This is the chat endpoint."}

@router.post("/embed", response_model = EmbeddingResponseSchema)
async def embed_text(request: TextRequestSchema):
    try:
        embedding = text_to_embedding(request.text)
        #retriever.obtain_similar_text(request.text)
        #upserter.insert(retriever.text)
        return {"text": request.text, "embedding": embedding}
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))