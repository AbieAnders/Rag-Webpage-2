from fastapi import APIRouter
from app.schemas.request import ChatRequestSchema

router = APIRouter()

@router.post("/chat")
async def send_chat_message(message: ChatRequestSchema):  # Expecting a JSON body
    # Here you can process the message
    print({"message": f"Received input: {message.user_input}"})
    return {"message": f"Received input: {message.user_input}"}
