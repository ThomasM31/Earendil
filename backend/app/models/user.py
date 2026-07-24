import datetime as dt
import sqlalchemy as sql
from db.database import Base

class User(Base):
    """
        Simple SQL for a database user
    """
    __tablename__ = "users"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    first_name = sql.Column(sql.String, index=True)
    last_name = sql.Column(sql.String, index=True)
    email = sql.Column(sql.String, index=True, unique=True)
    hashed_password = sql.Column(sql.String)
    date_created = sql.Column(sql.DateTime, default=dt.datetime.now(dt.timezone.utc)) 

"""
class Article(Base):
    
        #PDF Article & related information 
    
    __tablename__ = "articles"
    doi = sql.Column(sql.String, primary_key=True, index=True)
    title = sql.Column(sql.String)
    journal = sql.Column(sql.String, index=True)
    volume = sql.Column(sql.Integer)
    issue = sql.Column(sql.Integer)
    date = sql.Column(sql.DateTime)
    first_author = sql.Column(sql.String, index=True)
    authors = sql.Column(sql.String, index=True)
    email = sql.Column(sql.String, index=True, unique=True)
"""