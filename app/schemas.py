from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StudentBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    date_of_birth: str = Field(..., min_length=4, max_length=20)
    email: EmailStr
    phone: str = Field(..., min_length=7, max_length=20)
    course: str | None = Field(default=None, max_length=100)
    address: str | None = Field(default=None, max_length=250)
    enrollment_date: str | None = Field(default=None, max_length=20)


class StudentCreate(StudentBase):
    pass


class StudentUpdate(StudentBase):
    pass


class StudentResponse(StudentBase):
    student_id: int
    model_config = ConfigDict(from_attributes=True)
