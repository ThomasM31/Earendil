from datetime import timedelta
import os
from dotenv import load_dotenv
# FastAPI
from fastapi import HTTPException, Depends, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
# SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import func, select
# Internal
from app.models.user import User
from app.schemas.user import Token
from app.db.database import get_db
from app.schemas.user import UserCreate, UserPublic, UserPrivate, UserUpdate, UserLogin
from app.auth.security import hash_password, verify_password, oauth2_scheme
from app.auth.jwt import create_access_token, verify_access_token

router = APIRouter(prefix="/users", 
                   tags=["Users"])

# Access environment variables
load_dotenv()
access_token_expire_minutes = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

# Define GET-functionality
@router.get("/", response_model=list[UserPrivate])
def get_users(db: Session = Depends(get_db)):
    """
        Fetch all users from database
    """
    users = db.query(User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="No users found")
    
    return users

@router.get("/me", response_model=UserPrivate)
def get_current_user(token: str, db: Session = Depends(get_db)):
    """
        Get currently authorized user, validates token, gets user information
    """
    user_id = verify_access_token(token)
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Invalid or expired token")

    # Try to convert to int, defensive against bad JWT
    try:
        user_id_int = int(user_id)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid or expired token")

    user = db.query(User).filter(User.id == user_id_int).first()

    # Check if user exists
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="User not found")

    """return_user = UserPrivate(id=user.id,
                                username=user.username,
                                email=user.email,
                                name=user.name,
                                date_created=user.date_created)"""
    return user

@router.get("/{user_id}", response_model=UserPublic)
def get_user(user_id: str, db: Session = Depends(get_db)):
    """
        Find certain user
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, 
                            detail="User not found")
    
    return user

@router.post("/token", response_model=Token)
def login_for_access_token(user_data: UserLogin, db: Session = Depends(get_db)):
    # Look up user by username (case-insensitive)
    user = db.query(User).filter(func.lower(User.username) == user_data.username).first()

    # Verify user exists and password is correct
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password")

    # Create access token with user id as subject
    access_token_expires = timedelta(minutes=access_token_expire_minutes)
    access_token = create_access_token(data={"sub": str(user.id)}, expires_delta=access_token_expires)

    return Token(access_token=access_token, token_type="bearer")

    
# Define POST-functionality
@router.post("/register", status_code=status.HTTP_201_CREATED)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    """
        Create a new user and add to database
    """
    # Check for existing user, not case sensitive
    existing_user = db.query(User).filter(func.lower(User.username) == user.username.lower()).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Username already exists")

    # Same for email
    existing_email = db.query(User).filter(func.lower(User.email) == user.email.lower()).first()
    if existing_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Email already exists")
        
    # Create actual user with essential information, hash password
    new_user = User(email=user.email.lower(),
                username=user.username,
                name=user.name, 
                hashed_password=hash_password(user.password))

    # Update table with changes
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Create to hide password
    return_user = UserPrivate(id=new_user.id,
                              username=new_user.username,
                              email=new_user.email,
                              name=new_user.name,
                              date_created=new_user.date_created)

    return return_user

# Define DELETE-functionality
@router.delete("/", response_model=str)
def delete_all_users(db: Session = Depends(get_db)):
    """
        WARNING: Removes every single user from the database
    """
    users = get_users(db)
    for user in users:
        db.delete(user)

    db.commit()

    return "All users deleted!!!"

@router.delete("/{user_id}", response_model=str)
def delete_user(user_id: str, db:Session = Depends(get_db)):
    """
        Delete specific user from database
    """
    user = db.query(User).filter(User.username == user_id).first()

    if user:
        db.delete(user)
        db.commit()
    else:
        raise HTTPException(status_code=404, 
                            detail="User not found")
    
# Define PUT-functionality
@router.patch("/{user_id}")
def update_user(user_id: str, user_update: UserUpdate, db: Session = Depends(get_db)):
    """
        Update either email or password for user
    """

    # Find user in db
    user = db.query(User).filter(func.lower(User.username) == user_id.lower()).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="User not found")

    # If user wants to switch to username or already they already have 
    if user_update.username.lower() != user.username.lower() or user_update.email.lower() != user.email.lower():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Username or email already in use by requested user")
    
    # If user wants to swith username 
    if user_update.username is not None:
        existing_username = db.query(User).filter(func.lower(User.username) == user_update.username.lower()).first()
        # Check if new username is already in use
        if existing_username:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                                detail="Username already exists")

    # If user wants to swith email 
        if user_update.email is not None:
            existing_email = db.query(User).filter(func.lower(User.email) == user_update.email.lower()).first()
            # Check if new email is already in use
            if existing_email:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                                    detail="Email already registered")
    
    # Update necessary
    if user_update.username is not None:
        user.username = user_update.username
    if user_update.email is not None:
        user.email = user_update.email.lower()

    # Update table with changes
    db.commit()
    db.refresh(user)

    return user