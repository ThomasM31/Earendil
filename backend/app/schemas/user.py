from pydantic import BaseModel, Field, ConfigDict
import datetime as dt
from typing import Optional

# These are set on account creation, date_created will be generated
class UserCreate(BaseModel):
    email: str = Field(max_length=120)
    name: str = Field(max_length=70)
    username: str = Field(min_length=1, max_length=50)
    password: str = Field(min_length=8)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "username": "MyUserName1",
                "name": "FirstName LastName",
                "email": "UserEmail@example.com",
                "password": "SecurePassword123"
            }
        }
    )

class UserUpdate(BaseModel):
    username: str | None = Field(default=None, min_length=1, max_length=50)
    email: str | None = Field(default=None, max_length=120)

class UserLogin(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    password: str = Field(min_length=8)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "username": "MyUserName1",
                "password": "SecurePassword123" 
            }
        }
    )

class UserPublic(BaseModel):
    username: str
    name: Optional[str] = None
    date_created: dt.datetime

    model_config = {"from_attributes":True}

class UserPrivate(UserPublic):
    email: str


class Token(BaseModel):
    access_token: str
    token_type: str
