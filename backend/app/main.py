#raise RuntimeError("THIS IS THE FILE I AM EDITING")
import uvicorn
from pydantic import BaseModel
import uuid
import datetime as dt
from typing import Optional
# FastAPI
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
# Internal
from app.models.user import *
from app.db.database import engine, Base, get_db
# SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import text, update

# Setup the database tables & API
Base.metadata.create_all(bind=engine)
app = FastAPI()

class Status(BaseModel):
    status: str

# These are set on account creation, date_created will be generated
class UserCreate(BaseModel):
    """
        Information needed for account creation
    """
    email: str
    username: str
    # TODO: add password

class UserResponse(BaseModel):
    """
        Class for returning info from users
    """
    username: str
    email: str
    name: Optional[str] = None
    hashed_password: Optional[str] = None
    date_created: dt.datetime

    model_config = {"from_attributes":True}

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
    #print("Getting users...")
    users = db.query(User).all()

    #TEST
    #print(f"USERS: {users[0].__dict__}")

    return users
    
# Define POST-functionality
@app.post("/users/register")
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    # Create actual user with essential information
    user = User(email=user_data.email,
                username=user_data.username)

    # Att user to table
    db.add(user)
    # Update table with changes
    db.commit()
    db.refresh(user)

    return user

#@app.post("auth/login")

# Define DELETE-functionality
@app.delete("/users", response_model=str)
def delete_all_users(db: Session = Depends(get_db)):
    users = get_users(db)
    for user in users:
        db.delete(user)

    db.commit()

    return "All users deleted"
    
# Define PUT-functionality
@app.put("/users")
def change_user_email(username:str, 
                      email_to: str, 
                      db: Session = Depends(get_db)):
    # Find user in db
    user = db.get(User, username)

    # Change email
    user.email = email_to

    # Update table with changes
    db.commit()
    db.refresh(user)

    return user

@app.put("/users")
def change_username(email: str, 
                    username_to: str, 
                    db: Session = Depends(get_db)):
    # Find user in db
    user = db.get(User, email)

    # Change email
    user.username = username_to

    # Update table with changes
    db.commit()
    db.refresh(user)

    return user

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)