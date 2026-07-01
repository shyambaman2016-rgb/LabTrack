from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.services.user_service import register_user

from app.schemas.user import UserCreate, UserResponse
from app.schemas.user import UserLogin
from app.services.user_service import login_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return register_user(db, user)

@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    return login_user(db, user)