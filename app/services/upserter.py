import os
#from pinecone import Pinecone, ServerlessSpec
from pydantic import BaseModel
import numpy as np

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY", "")
'''
pc = Pinecone(api_key = PINECONE_API_KEY, environment = "us-west1-gcp")

index_parameters = {
    "open-embedding-model": {
        "dimension": 1536,
        "metric": "cosine",
        "replicas": 0,
        "description": "Index for OpenAI embeddings"
    }
}
test_index = "sparse-index"

print(pc.list_indexes().names())

if not pc.has_index(name = test_index):
    pc.create_index(
        name = test_index,
        dimension = 512,
        metric = "cosine",
        spec = ServerlessSpec(
            cloud = "aws",
            region = "us-east-1"
        ) 
    )

index = pc.Index(test_index)


test_query = "Tell them to bring out the lobster"
test_vector_embedding = np.random.random(512).tolist()
print(test_vector_embedding)
metadata = { 
    "query": test_query,
    "additional info": "This is some sample text"
}

index.upsert(
    index_name = test_index,
    vectors = [("id1", test_vector_embedding, metadata)]
)'
''
'''


