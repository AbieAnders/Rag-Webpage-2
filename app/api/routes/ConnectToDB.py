from fastapi import APIRouter, HTTPException
from app.schemas.response import WeaviateStatusSchema
from app.services.dbconnector import connect_to_db
from typing import Any

router = APIRouter()

@router.post("/connect_weaviate", response_model = WeaviateStatusSchema)
async def connect_to_weaviate():
    client = None
    try:
        client = connect_to_db()
        return { "client": client }
    except Exception as e:
        raise HTTPException(status_code = 500, detail = {"error": str(e)})    










            