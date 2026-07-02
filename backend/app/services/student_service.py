from sqlalchemy.orm import Session

from app.models.student import Student
from app.schemas.student import StudentCreate

def create_student(
    db: Session,
    student: StudentCreate
):
    new_student = Student(
        enrollment_no=student.enrollment_no,
        name=student.name,
        email=student.email,
        department=student.department,
        semester=student.semester
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student