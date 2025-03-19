from google import genai

client = genai.Client(api_key = "GEMINI_API_KEY")

def text_to_embedding(text):
    result = client.models.embed_content(
        model = "gemini-embedding-exp-03-0",
        contents = text,
    )
    #print(result.embeddings)
    return result.embeddings