import sqlalchemy as sql
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.orm as orm


DATABASE_URL = "postgresql://myuser:HighBass123!?@localhost/fastapi_database"

engine = sql.create_engine(DATABASE_URL)

SessionLocal = orm.sessionmaker(autoflush=False, bind=engine)

Base = declarative.declarative_base()

