from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.services.user_service import register_user

from app.schemas.user import UserCreate, UserResponse
from app.schemas.user import UserLogin
from fastapi.security import OAuth2PasswordRequestForm

from app.services.user_service import login_user

from app.database.dependencies import get_current_user
from app.models.user import User

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
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return login_user(db, form_data)

@router.get("/me",
            response_model=UserResponse)
def get_me(
    current_user: User = Depends(get_current_user)
):
    return current_user