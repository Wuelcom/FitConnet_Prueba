from pydantic import BaseModel
from typing import Optional

class RutinaBase(BaseModel):
    id_usuario: int
    id_objetivo: Optional[int] = None
    nombre_rutina: str
    descripcion: Optional[str] = None

class RutinaCreate(RutinaBase):
    pass

class RutinaUpdate(RutinaBase):
    pass

class RutinaOut(RutinaBase):
    id_rutina: int
    class Config:
        from_attributes = True
