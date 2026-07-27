import uvicorn
from pydantic import BaseModel
import uuid
# FastAPI
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
# Internal
from models.user import *
from db.database import engine, Base, get_db
# SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import text

# Setup the database tables & API
Base.metadata.create_all(bind=engine)
app = FastAPI()

class Status(BaseModel):
    status: str

# These are set on account creation, id_internal will be generated
class UserCreate(BaseModel):
    email: str
    username: str

class UserResponse(BaseModel):
    email: str
    username: str
    name: str | None

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

@app.get("/db-test")
def db_test(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1"))
    return {
        "database": result.scalar()
    }

@app.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

# Define POST-functionality
@app.post("/users")
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    # Create actual user with essential information
    user = User(email=user_data.email,
                username=user_data.username)

    # Att user to table
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

# Define DELETE-functionality
@app.delete("/users")
def delete_all_users(db: Session = Depends(get_db)):
    users = get_users(db)
    for user in users:
        db.delete(user)

    db.commit()

    return "All users deleted"
    
"""
# Define PUT-functionality
@app.put("/status", response_model=Status)
def update_status(status: Status):
    memory_db["status"] = status.status
    return status
"""

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

