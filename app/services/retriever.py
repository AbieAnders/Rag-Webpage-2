import os
from pinecone import Pinecone

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY", "")

pc = Pinecone(api_key = PINECONE_API_KEY, environment = "us-west1-gcp")

def similarity_search(text):
    test_index = "quickstart-text-embeddings"
    index = pc.Index(test_index)
    query_vector = [0.1, 0.2, 0.3, 0.4]

    results = index.query(query_vector, top_k = 5, include_metadata = True)

    for match in results['matches']:
        print(f"ID: {match['id']}, Score: {match['score']}")
        if 'metadata' in match:
            print(f"Metadata: {match['metadata']}")