from pydantic import BaseModel
from typing import Optional

class LogroBase(BaseModel):
    nombre: str
    descripcion: str
    tipo: str
    puntos: Optional[int] = 10

class LogroCreate(LogroBase):
    pass

class LogroOut(LogroBase):
    id_logro: int
    class Config:
        from_attributes = True
