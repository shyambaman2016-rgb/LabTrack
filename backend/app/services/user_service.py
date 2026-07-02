from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.schemas.user import UserLogin

from app.core.security import get_password_hash
from app.core.security import verify_password
from app.core.security import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

def register_user(
    db: Session,
    user: UserCreate
):
    new_user = User(
        name=user.name,
        email=user.email,
        password=get_password_hash(user.password),
        role="student"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login_user(
    db: Session,
    form_data: OAuth2PasswordRequestForm
):
    db_user = db.query(User).filter(
        User.email == form_data.username
    ).first()

    if not db_user:
        return {"message": "Invalid Credentials"}

    if not verify_password(
        form_data.password,
        db_user.password
    ):
        return {"message": "Invalid Credentials"}

    access_token = create_access_token(
    data={"sub": db_user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }