from langchain.vectorstores import FAISS
from app.services.embedder import text_to_embedding
import faiss

class VectorRetriever:
    def __init__(self):
        self.index = faiss.IndexFlatL2(1536)
    
    def add_text(self, text):
        vector = text_to_embedding(text)
        self.index.add(vector)
    
    def search(self, query):
        vector = text_to_embedding(query)
        distances, indices = self.index.search(vector, k = 5)
        return indices
    
retiever = VectorRetriever()