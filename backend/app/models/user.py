import datetime as dt
#from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    pass
    
class User(Base):
    """
        structure for a database user
    """
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(index=True, unique=True)
    last_name: Mapped[str] = mapped_column(index=True)
    first_name: Mapped[str]
    hashed_password: Mapped[str]
    #date_created: Mapped[] = Column(DateTime, default=dt.datetime.now(dt.timezone.utc)) TODO: How to do this???

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