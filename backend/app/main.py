import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Annotated

class Status(BaseModel):
    status: str

class Message(BaseModel):
    name: str

class Messages(BaseModel):
    messages: List[Message]

app = FastAPI()

origins = [
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
                   )

memory_db = {
    "greeting": "Research Assistant API",
    "status": "healthy",
    "messages": [],
            }

# Check available methods
#for route in app.routes:
#    print(route.path, route.methods)

# @app: POST, GET, DELETE, PUT

# Define GET-functionality
@app.get("/greeting", response_model=Message)
def get_greeting():
    return Message(name=memory_db["greeting"])

@app.get("/messages", response_model=Messages)
def get_messages():
    return Messages(messages=memory_db["messages"])

@app.get("/status", response_model=Status)
def get_status():
    return Status(status=memory_db["status"])


# Define POST-functionality
@app.post("/messages", response_model=Message)
def add_message(message: Message):
    memory_db["messages"].append(message)
    return message


# Define PUT-functionality
@app.put("/status", response_model=Status)
def update_status(status: Status):
    memory_db["status"] = status.status
    return status


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

