from src.rag import chat_with_rag
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


import uvicorn

class ChatInput(BaseModel):
    input: str

app = FastAPI()


@app.post("/chat")
async def chat(input: ChatInput):
    input_dict = input.model_dump()
    answer = chat_with_rag(input_dict["input"])
    return {
        "text": answer
    }

#load static html after post because getting method not allowerd
app.mount("/", StaticFiles(directory="static", html=True), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[*],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)