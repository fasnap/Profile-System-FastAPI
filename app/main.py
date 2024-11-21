from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, utils
from .database import engine, Base, get_db

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

@app.post("/create-profile", response_model=schemas.StudentResponse)
def create_profile(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    # Validate password (custom validation)
    utils.validate_password(student.password)

    # Check if email already exists
    existing_student = db.query(models.Student).filter(models.Student.email == student.email).first()
    if existing_student:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create and save student profile
    created_student = crud.create_student(db, student)
    return schemas.StudentResponse(
        name=created_student.name,
        email=created_student.email,
        phone=created_student.phone,
    )
