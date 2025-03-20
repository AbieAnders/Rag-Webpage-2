from fastapi import APIRouter


router = APIRouter()
'''
@router.post("/insert_weaviate")
async def insert_to_weaviate(client):
    try:
        questions = client.collections.create(
            name = "Article",
            vectorizer_config=Configure.Vectorizer.text2vec_openai(),
            properties=[
                Property(name="title", data_type=DataType.TEXT),
                Property(name="body", data_type=DataType.TEXT),
            ]
        )
        print("Connected to weaviate and collection created")
        return WeaviateStatus(message = "Connected to weaviate and collection created", is_connected = True)
    except Exception as e:
        print(e.args[0])
        print("Failed to create collection")
        raise HTTPException(status_code = 500, detail = f"Failed to create collection")'''