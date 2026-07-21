import datetime as dt
import sqlalchemy as sql
import db.database as db

"""
class Contact(db.Base):
    
    #Simple SQL for a contact
    
    __tablename__ = "contacts"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    first_name = sql.Column(sql.String, index=True)
    last_name = sql.Column(sql.String, index=True)
    email = sql.Column(sql.String, index=True, unique=True)
    phone_number = sql.Column(sql.String, index=True, unique=True)
    date_created = sql.Column(sql.DateTime, default=dt.datetime.now(dt.timezone.utc)) 

"""