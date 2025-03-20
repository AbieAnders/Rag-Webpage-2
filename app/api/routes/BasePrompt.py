from fastapi import APIRouter
from app.schemas.request import ChatRequestSchema

router = APIRouter()

@router.post("/base_prompt")
async def set_base_prompt(message: ChatRequestSchema):
    #ask llm to create good keywords for duck duck go search
    #use that in the ddg_search function and get the response.
    #use that response to get the links
    #go into each link and extract static html
    #convert static html to markdown
    #use an llm to fill the schema of the weaviate database
    #ensure that recursive link search is done within the markdown until the schema is filled
    print({"message": f"Received input: {message.user_input}"})
    return {"message": f"Received input: {message.user_input}"}
