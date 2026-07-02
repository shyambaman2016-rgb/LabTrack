from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.core.permissions import require_roles

from app.schemas.student import StudentCreate, StudentResponse
from app.services.student_service import create_student
from app.models.user import User

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.post(
    "/",
    response_model=StudentResponse
)
def add_student(
    student: StudentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_roles(["faculty", "admin"])
    )
):
    return create_student(db, student)
