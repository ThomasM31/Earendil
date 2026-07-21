import db.database as _database
import models.models as _models

def add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)

