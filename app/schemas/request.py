from pydantic import BaseModel

class ChatRequestSchema(BaseModel):
    user_input: str

class TextRequestSchema(BaseModel):
    text: str