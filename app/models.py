from sqlalchemy import Column, Integer, String
from .database import Base


class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    date_of_birth = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    phone = Column(String, nullable=False)
    course = Column(String, nullable=True)
    address = Column(String, nullable=True)
    enrollment_date = Column(String, nullable=True)
