from fastapi import FastAPI
from app.config import settings
from app.api.routes import ConnectToDB, ProcessText, RetrieveText, ScrapeData, ChatMessage  #importing routes

app = FastAPI(title = settings.APP_NAME, debug = settings.DEBUG)

#app.include_router(ScrapeData.router, prefix = "/api")
#app.include_router(ConnectToDB.router, prefix = "/api")
#app.include_router(ProcessText.router, prefix = "/api")
#app.include_router(RetrieveText.router, prefix = "/api")
app.include_router(ChatMessage.router, prefix ="/api")

@app.get("/")
async def root():
    # Simulates the root landing page.
    return {"message": f"Welcome to {settings.APP_NAME}"}