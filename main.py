from src.rag import chat_with_rag
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class ChatInput(BaseModel):
    input: str

app = FastAPI()


@app.post("/chat")
async def chat(input: ChatInput):
    input_dict = input.model_dump()
    return chat_with_rag(input_dict["input"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)