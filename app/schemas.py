from pydantic import BaseModel, EmailStr, constr

class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str = None
    password: str
class StudentResponse(BaseModel):
    name: str
    email: EmailStr
    phone: str = None

    class Config:
        orm_mode = True