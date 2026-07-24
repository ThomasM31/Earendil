import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Annotated
from models.user import User
from db.database import engine, Base
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)
app = FastAPI()

class Status(BaseModel):
    status: str

class Message(BaseModel):
    name: str

class Messages(BaseModel):
    messages: List[Message]

#db_dependency = Annotated[Session, Depends(get_db)]

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

# @app: POST, GET, DELETE, PUT
# Define GET-functionality
@app.get("/")
def root():
    return {
        "message": "Research Assistant API"
    }

@app.get("/status")
def get_status():
    return {
        "status": "healthy"
    }

"""
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
"""

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

