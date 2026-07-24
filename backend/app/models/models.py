import datetime as dt
import sqlalchemy as sql
from db.database import Base

class User(Base):
    """
        Simple SQL for a contact
    """
    __tablename__ = "users"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    first_name = sql.Column(sql.String, index=True)
    last_name = sql.Column(sql.String, index=True)
    email = sql.Column(sql.String, index=True, unique=True)
    phone_number = sql.Column(sql.String, index=True, unique=True)
    date_created = sql.Column(sql.DateTime, default=dt.datetime.now(dt.timezone.utc)) 

class Article(Base):
    """
        PDF Article information 
    """
    __tablename__ = "articles"
    doi = sql.Column(sql.String, primary_key=True, index=True)
    title = sql.Column()
    author = sql.Column(sql.String)
    email = sql.Column(sql.String, index=True, unique=True)
    date = sql.Column(sql.DateTime)

    