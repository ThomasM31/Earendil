#raise RuntimeError("THIS IS THE FILE I AM EDITING")
import uvicorn
# FastAPI
from fastapi import FastAPI, Depends, Request, status
from fastapi.middleware.cors import CORSMiddleware
# Internal
from app.db.database import engine, Base, get_db
from app.routers import user, auth
# SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import text

# Setup the database tables & API
#Base.metadata.create_all(bind=engine) # Can be run from here without Alembic
app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
                   )

# Add routers here
app.include_router(user.router)
app.include_router(auth.router)

# Default HTTP
@app.get("/")
async def root():
    return {
        "message": "Research Assistant API"
    }


@app.get("/health")
def get_status():
    return {
        "status": "healthy"
    }

@app.get("/db-test")
def db_test(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1"))
    return {
        "database": result.scalar()
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)