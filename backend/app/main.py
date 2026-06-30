from fastapi import FastAPI

from app.database.base import Base
from app.database.connection import engine
from app.api.user import router as user_router
# Import all models
from app.models.user import User

app = FastAPI(
    title="LabTrack API",
    version="1.0.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)
app.include_router(user_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to LabTrack API 🚀"
    }