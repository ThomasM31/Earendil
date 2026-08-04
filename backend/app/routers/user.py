# FastAPI
from fastapi import HTTPException, Depends, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
# SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import func, select
# Internal
from app.models.user import User
from app.db.database import get_db
from app.schemas.user import UserCreate, UserPublic, UserPrivate
from app.auth.security import hash_password, verify_password
from app.auth.jwt import create_access_token, verify_access_token
from datetime import timedelta

router = APIRouter(prefix="/users", 
                   tags=["Users"])

# Define GET-functionality
@router.get("/", response_model=list[UserPrivate])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    
    return users

@router.get("/{username}", response_model=UserPublic)
def get_user(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
    
# Define POST-functionality
@router.post("/register", response_model=UserPrivate, status_code=status.HTTP_201_CREATED)
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(User.username == user_data.username)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")

    existing_email = db.query(User).filter(User.email == user_data.email)
    if existing_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
        
    # Create actual user with essential information, hash password
    user = User(email=user_data.email,
                username=user_data.username,
                name=user_data.name, 
                hashed_password=hash_password(user_data.password))

    # Att user to table
    db.add(user)
    # Update table with changes
    db.commit()
    db.refresh(user)

    return user

# Define DELETE-functionality
@router.delete("/", response_model=str)
def delete_all_users(db: Session = Depends(get_db)):
    users = get_users(db)
    for user in users:
        db.delete(user)

    db.commit()

    return "All users deleted!!!"

@router.delete("/{username}", response_model=str)
def delete_user(username: str, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()

    if user:
        db.delete(user)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="User not found")
    
# Define PUT-functionality
@router.put("/{username}")
def change_user_email(username: str, 
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

@router.put("/{username}")
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