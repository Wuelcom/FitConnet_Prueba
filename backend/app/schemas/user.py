from pydantic import BaseModel, EmailStr
from typing import Optional, Literal
from datetime import date, datetime

class UserBase(BaseModel):
    nombre: str
    correo_electronico: EmailStr
    fecha_nacimiento: Optional[date] = None
    telefono: Optional[str] = None
    id_objetivo: Optional[int] = None
    edad: Optional[int] = None
    peso: Optional[float] = None
    altura: Optional[float] = None
    genero: Optional[Literal['M', 'F', 'Otro']] = None

class UserCreate(UserBase):
    contrasena: str
    edad: int
    peso: float
    altura: float
    genero: Literal['M', 'F', 'Otro']

class UserUpdate(BaseModel):
    nombre: Optional[str] = None
    correo_electronico: Optional[EmailStr] = None
    contrasena: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    telefono: Optional[str] = None
    id_objetivo: Optional[int] = None
    edad: Optional[int] = None
    peso: Optional[float] = None
    altura: Optional[float] = None
    genero: Optional[Literal['M', 'F', 'Otro']] = None

class UserOut(UserBase):
    id_usuario: int
    fecha_registro: datetime

    class Config:
        from_attributes = True
