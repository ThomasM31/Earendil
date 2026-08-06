import datetime as dt
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base
from typing import Optional

class Document(Base):
    """
        SQL structure for a document
    """
    __tablename__ = "documents"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    filename: Mapped[str] = mapped_column(index=True)
    owner_id: Mapped[int] = mapped_column(index=True)
    file_path: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(index=True)
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