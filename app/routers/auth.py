# FastAPI
from fastapi import APIRouter, Depends, HTTPException, status
# SQLAlchemy
from sqlalchemy.orm import Session
# Internal
from app.db.database import get_db
from app.models.user import User
from app.schemas.user import Token, UserLogin
from app.auth.security import verify_password
from app.auth.jwt import create_access_token

router = APIRouter(prefix="/auth", 
                   tags=["Authentication"])

@router.post("/login", response_model=Token)
def login(user_data: UserLogin, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.username == user_data.username).first()

    # User does not exist in database
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    # Incorrect passowrd for user
    if not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = create_access_token({"sub": str(user.username)})

    return {"access_token": token, "token_type": "bearer"}
