from sqlalchemy.orm import Session
from . import models, schemas

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(
        name=student.name,
        email=student.email,
        phone=student.phone,
        password=student.password  # Password should be hashed in production
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student