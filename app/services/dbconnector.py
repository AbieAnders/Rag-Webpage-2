from pydantic import BaseModel
import weaviate
from weaviate.auth import Auth
from fastapi import HTTPException
import os

def connect_to_db():
    client = None
    try:
        #print("Attempting connection to weaviate")
        client = weaviate.connect_to_weaviate_cloud(
            cluster_url = os.getenv("WEAVIATE_URL"),
            auth_credentials = Auth.api_key(os.getenv("WEAVIATE_API_KEY")),
            skip_init_checks = True
        )
        if(client.is_ready()):
            return client
        else:
            raise HTTPException(status_code = 500, detail = "Weaviate instance is not ready")
    except Exception as e:
        #print("Failed to connect to weavite")
        raise HTTPException(status_code = 500, detail = {"error": str(e)})
    
def disconnect_from_db(client):
    return client.close()