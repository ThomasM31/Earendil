import datetime as dt
from sqlalchemy.orm import Mapped, mapped_column
from db.database import Base
    
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
