from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from .database import get_db
from . import crud, schemas

router = APIRouter(prefix="/students", tags=["Students"])


@router.post("/", response_model=schemas.StudentResponse, status_code=201)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_student(db, student)
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc))


@router.get("/", response_model=list[schemas.StudentResponse])
def get_students(
    name: str | None = Query(default=None),
    course: str | None = Query(default=None),
    db: Session = Depends(get_db),
):
    students = crud.get_students(db)
    if name:
        students = [s for s in students if name.lower() in s.name.lower()]
    if course:
        students = [s for s in students if course.lower() in (s.course or "").lower()]
    return students


@router.get("/{student_id}", response_model=schemas.StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.put("/{student_id}", response_model=schemas.StudentResponse)
def update_student(
    student_id: int,
    student: schemas.StudentUpdate,
    db: Session = Depends(get_db),
):
    try:
        updated = crud.update_student(db, student_id, student)
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc))

    if updated is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated


@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_student(db, student_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully", "student_id": student_id}
