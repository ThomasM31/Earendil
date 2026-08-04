import datetime as dt
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base
from typing import Optional
    
class User(Base):
    """
        SQL structure for a user
    """
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(unique=True, index=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    name: Mapped[str]
    hashed_password: Mapped[str]
    date_created: Mapped[dt.datetime] = mapped_column(index=True, default=str(dt.datetime.now(dt.timezone.utc)))

"""
class Article(Base):
    
        #PDF Article & related information 
    
    __tablename__ = "articles"
    doi = Column(String, primary_key=True, index=True)
    title = Column(String)
    journal = Column(String, index=True)
    volume = Column(Integer)
    issue = Column(Integer)
    date = Column(DateTime)
    first_author = Column(String, index=True)
    authors = Column(String, index=True)
    email = Column(String, index=True, unique=True)
"""