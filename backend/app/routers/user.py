# FastAPI
from fastapi import HTTPException, Depends, status, APIRouter
# SQLAlchemy
from sqlalchemy.orm import Session
# Internal
from app.models.user import User
from app.db.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.auth.security import hash_password

router = APIRouter(prefix="/users", tags=["Users", "User"])

# Define GET-functionality
@router.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.get("/users/{username}", response_model=UserResponse)
def get_user(username:str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
    
# Define POST-functionality
@router.post("/users/register", status_code=status.HTTP_201_CREATED)
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
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
@router.delete("/users", response_model=str)
def delete_all_users(db: Session = Depends(get_db)):
    users = get_users(db)
    for user in users:
        db.delete(user)

    db.commit()

    return "All users deleted"
    
# Define PUT-functionality
@router.put("/users/{username}")
def change_user_email(username:str, 
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

@router.put("/users/{username}")
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