from datetime import datetime, timedelta, UTC
import jwt
from app.config import settings

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
        Create access token from username
    """
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=int(settings.access_token_expire_minutes))

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        payload=to_encode,
        key=settings.secret_key,
        algorithm=settings.algorithm
    )

    return encoded_jwt

def verify_access_token(token: str) -> str | None:
    """
        Verify a JWT access token and return subject (id) if valid
    """
    try:
        payload = jwt.decode(
            jwt=token,
            key=settings.secret_key,
            algorithms=[settings.algorithm],
            options={"require": ["exp", "sub"]}
        )
    except jwt.InvalidTokenError:
        return None
    else:
        return payload.get("sub")