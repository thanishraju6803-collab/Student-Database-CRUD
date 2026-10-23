from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from . import models, schemas


def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    try:
        db.commit()
        db.refresh(db_student)
    except IntegrityError:
        db.rollback()
        raise ValueError("A student with this email already exists.")
    return db_student


def get_students(db: Session):
    return db.query(models.Student).order_by(models.Student.student_id).all()


def get_student(db: Session, student_id: int):
    return (
        db.query(models.Student)
        .filter(models.Student.student_id == student_id)
        .first()
    )


def update_student(db: Session, student_id: int, student: schemas.StudentUpdate):
    db_student = get_student(db, student_id)
    if db_student is None:
        return None

    for key, value in student.model_dump().items():
        setattr(db_student, key, value)

    try:
        db.commit()
        db.refresh(db_student)
    except IntegrityError:
        db.rollback()
        raise ValueError("A student with this email already exists.")
    return db_student


def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)
    if db_student is None:
        return None

    db.delete(db_student)
    db.commit()
    return db_student
