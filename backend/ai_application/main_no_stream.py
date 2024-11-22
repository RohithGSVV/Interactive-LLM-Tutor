#!/usr/bin/env python3
#      _    ___      _                _ _           _   _             
#     / \  |_ _|    / \   _ __  _ __ | (_) ___ __ _| |_(_) ___  _ __  
#    / _ \  | |    / _ \ | '_ \| '_ \| | |/ __/ _` | __| |/ _ \| '_ \ 
#   / ___ \ | |   / ___ \| |_) | |_) | | | (_| (_| | |_| | (_) | | | |
#  /_/   \_\___| /_/   \_\ .__/| .__/|_|_|\___\__,_|\__|_|\___/|_| |_|
#                        |_|   |_|                                    
import os
import time
import json
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from langchain_ollama import OllamaLLM
from langchain.callbacks.base import BaseCallbackHandler

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ollama_base_url = os.getenv("OLLAMA_BASE_URL")

class StreamingCallbackHandler(BaseCallbackHandler):
    def __init__(self):
        self.tokens = []

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.tokens.append(token)

class CompletionRequest(BaseModel):
    model: str
    prompt: str
    max_tokens: int = 100
    temperature: float = 0.7
    stream: bool = False

class ChatCompletionRequest(BaseModel):
    model: str
    messages: list
    max_tokens: int = 100
    temperature: float = 0.7
    stream: bool = False

def create_stream_response(tokens, request_type):
    for token in tokens:
        if request_type == "completion":
            yield f"data: {json.dumps({'choices': [{'text': token}]})}\n\n"
        else:  # chat completion
            yield f"data: {json.dumps({'choices': [{'delta': {'content': token}}]})}\n\n"
    yield "data: [DONE]\n\n"

@app.post("/v1/completions")
async def create_completion(request: CompletionRequest):
    callback = StreamingCallbackHandler()
    # llm = Ollama(
    llm = OllamaLLM(
        base_url=ollama_base_url,
        model="llama3.1",
        callbacks=[callback],
        temperature=request.temperature,
        # max_tokens=request.max_tokens,
    )

    try:
        llm.invoke(request.prompt)
        response = "".join(callback.tokens)

        if request.stream:
            return StreamingResponse(create_stream_response(callback.tokens, "completion"), media_type="text/event-stream")
        else:
            return {
                "id": "cmpl-" + os.urandom(12).hex(),
                "object": "text_completion",
                "created": int(time.time()),
                "model": request.model,
                "choices": [
                    {
                        "text": response,
                        "index": 0,
                        "logprobs": None,
                        "finish_reason": "stop"
                    }
                ],
                "usage": {
                    "prompt_tokens": len(request.prompt.split()),
                    "completion_tokens": len(response.split()),
                    "total_tokens": len(request.prompt.split()) + len(response.split())
                }
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/v1/chat/completions")
async def create_chat_completion(request: ChatCompletionRequest):
    callback = StreamingCallbackHandler()
    llm = OllamaLLM(
        base_url=ollama_base_url,
        model="llama3.1",
        callbacks=[callback],
        temperature=request.temperature,
        # max_tokens=request.max_tokens,
    )

    try:
        prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in request.messages])
        # llm(prompt)
        llm.invoke(prompt)
        response = "".join(callback.tokens)

        if request.stream:
            return StreamingResponse(create_stream_response(callback.tokens, "chat"), media_type="text/event-stream")
        else:
            return {
                "id": "chatcmpl-" + os.urandom(12).hex(),
                "object": "chat.completion",
                "created": int(time.time()),
                "model": request.model,
                "choices": [
                    {
                        "index": 0,
                        "message": {
                            "role": "assistant",
                            "content": response
                        },
                        "finish_reason": "stop"
                    }
                ],
                "usage": {
                    "prompt_tokens": len(prompt.split()),
                    "completion_tokens": len(response.split()),
                    "total_tokens": len(prompt.split()) + len(response.split())
                }
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
