from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime

class UserBase(BaseModel):
    nombre: str
    correo_electronico: EmailStr
    fecha_nacimiento: Optional[date] = None
    telefono: Optional[str] = None
    id_objetivo: Optional[int] = None

class UserCreate(UserBase):
    contrasena: str

class UserUpdate(BaseModel):
    nombre: Optional[str] = None
    correo_electronico: Optional[EmailStr] = None
    contrasena: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    telefono: Optional[str] = None
    id_objetivo: Optional[int] = None

class UserOut(UserBase):
    id_usuario: int
    fecha_registro: datetime

    class Config:
        from_attributes = True
