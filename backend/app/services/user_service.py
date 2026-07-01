from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate

from app.core.security import get_password_hash

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