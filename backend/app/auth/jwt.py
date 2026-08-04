from datetime import datetime, timedelta, UTC
from jose import jwt

SECRET_KEY = "change-this-later"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, time_to_expire_minutes: int | None = None):

    to_encode = data.copy()

    if time_to_expire_minutes:
        expire = datetime.now(UTC) + timedelta(minutes=time_to_expire_minutes)
    else:
        expire = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt
