# Internal
from app.config import settings
# SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Create engine & session, acts as database representation 
engine = create_engine(url=settings.database_url)
SessionLocal = sessionmaker(autoflush=False, bind=engine)

# 
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#print("DATABASE_URL:", repr(DATABASE_URL))