from pydantic import BaseModel, EmailStr


class StudentCreate(BaseModel):
    enrollment_no: str
    name: str
    email: EmailStr
    department: str
    semester: int


class StudentResponse(BaseModel):
    id: int
    enrollment_no: str
    name: str
    email: EmailStr
    department: str
    semester: int

    class Config:
        from_attributes = True