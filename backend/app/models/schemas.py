from pydantic import BaseModel, Field
import datetime as dt
from typing import Optional

class Status(BaseModel):
    status: str

# These are set on account creation, date_created will be generated
class UserCreate(BaseModel):
    email: str = Field(max_length=120)
    username: str = Field(min_length=1, max_length=50)
    hashed_password: str = Field(min_length=8)

class UserResponse(BaseModel):
    username: str
    email: str
    name: Optional[str] = None
    hashed_password: Optional[str] = None
    date_created: dt.datetime

    model_config = {"from_attributes":True}

class Token(BaseModel):
    access_token: str
    token_type: str
