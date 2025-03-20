import asyncio
from google import genai
import logging

client = genai.Client(api_key = "GEMINI_API_KEY")

llm_model = "gemini-2.0-flash"
config = {"response_modalities": ["TEXT"]}

async def prompt_llm(prompt_text: str):
    try:
        async with client.aio.live.connect(model = llm_model, config = config) as session:
            await session.send(input = prompt_text, end_of_turn = True)
            async for response in session.receive():
                if response.text is not None:
                    return response.text
                else:
                    raise ValueError("No text response received from the model.")
    except Exception as e:
        logging.error(e)
        raise