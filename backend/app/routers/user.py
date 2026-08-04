# FastAPI
from fastapi import HTTPException, Depends, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
# SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import func, select
# Internal
from app.models.user import User
from app.db.database import get_db
from app.schemas.user import UserCreate, UserPublic, UserPrivate, UserUpdate
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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")
    
    return users

@router.get("/me", response_model=UserPrivate)
def get_current_user(token: str, db: Session = Depends(get_db)):
    """
        Get currently authorized user, validates token, gets user information
    """
    username = verify_access_token(token)
    if username is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")

    user = db.query(User).filter(User.username == username)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    return user

@router.get("/{username}", response_model=UserPublic)
def get_user(username: str, db: Session = Depends(get_db)):
    """
        Find certain user
    """
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
    """
        Create a new user and add to database
    """
    # Check for existing user, not case sensitive
    existing_user = db.query(User).filter(func.lower(User.username) == user_data.username.lower())
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")

    existing_email = db.query(User).filter(func.lower(User.email) == user_data.email.lower())
    if existing_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
        
    # Create actual user with essential information, hash password
    new_user = User(email=user_data.email.lower(),
                username=user_data.username,
                name=user_data.name, 
                hashed_password=hash_password(user_data.password))

    # Att user to table
    db.add(new_user)
    # Update table with changes
    db.commit()
    db.refresh(new_user)

    return new_user

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

@router.delete("/{username}", response_model=str)
def delete_user(username: str, db:Session = Depends(get_db)):
    """
        Delete specific user from database
    """
    user = db.query(User).filter(User.username == username).first()

    if user:
        db.delete(user)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="User not found")
    
# Define PUT-functionality
@router.patch("/{username}")
def update_user(username: str, 
                user_update: UserUpdate,
                db: Session = Depends(get_db)):

    # Find user in db
    user = db.query(User).filter(func.lower(User.username) == username.lower()).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    # If user wants to swith username & it is not the same as already in place
    if user_update.username is not None and user_update.username.lower() != user.username.lower():
        existing_username = db.query(User).filter(func.lower(User.username) == user_update.username.lower()).first()
        # Check if new username is already in use
        if existing_username:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")

    # If user wants to swith email & it is not the same as already in place
        if user_update.email is not None and user_update.email != user.email:
            existing_email = db.query(User).filter(func.lower(User.email) == user_update.email.lower()).first()
            # Check if new email is already in use
            if existing_email:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    # Update necessary
    if user_update.username is not None:
        user.username = user_update.username
    if user_update.email is not None:
        user.email = user_update.email.lower()

    # Update table with changes
    db.commit()
    db.refresh(user)

    return user