from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)
    bio: Optional[str] = ""

class UserLogin(BaseModel):
    username: str
    password: str

class UserUpdate(BaseModel):
    bio: Optional[str] = None

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    bio: Optional[str]
    class Config:
        orm_mode = True
