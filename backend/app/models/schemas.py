from pydantic import BaseModel
import datetime as dt
from typing import Optional

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