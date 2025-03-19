from pydantic import BaseModel
from typing import List

class EmbeddingResponseSchema(BaseModel):
    text: str
    embedding: List[float]

class WeaviateStatusSchema(BaseModel):
    message: str
    is_connected: bool