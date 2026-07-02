from fastapi import FastAPI

from app.database.base import Base
from app.database.connection import engine
from app.api.user import router as user_router
from app.api.student import router as student_router

# Import all models
from app.models.user import User
from app.models.student import Student

app = FastAPI(
    title="LabTrack API",
    version="1.0.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)
app.include_router(user_router)
app.include_router(student_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to LabTrack API 🚀"
    }