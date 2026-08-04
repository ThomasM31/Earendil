from datetime import datetime, timedelta, UTC
import jwt
import os
from dotenv import load_dotenv

# Access SECRET_KEY from .env
load_dotenv()
secret_key = os.getenv("SECRET_KEY")
algorithm = os.getenv("ALGORITHM")
access_token_expire_minutes = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

def create_access_token(data: dict, expires_time: timedelta | None = None):
    """
        Create access token from username
    """
    to_encode = data.copy()

    if expires_time:
        expire = datetime.now(UTC) + timedelta(minutes=expires_time)
    else:
        expire = datetime.now(UTC) + timedelta(minutes=int(access_token_expire_minutes))

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        payload=to_encode,
        key=secret_key,
        algorithm=algorithm
    )

    return encoded_jwt

def verify_access_token(token: str) -> str | None:
    """
        Verify a JWT access token and return subject (username) if valid
    """
    try:
        payload = jwt.decode(
            jwt=token,
            key=secret_key,
            algorithms=[algorithm],
            options={"require": ["exp", "sub"]}
        )
    except jwt.InvalidTokenError:
        return None
    else:
        return payload.get("sub")