from pydantic import BaseModel
from typing import Optional

class ProgresoBase(BaseModel):
    id_usuario: int
    peso_actual: Optional[float] = None
    grasa_corporal: Optional[float] = None
    masa_muscular: Optional[float] = None
    observaciones: Optional[str] = None

class ProgresoCreate(ProgresoBase):
    pass

class ProgresoOut(ProgresoBase):
    id_progreso: int
    class Config:
        from_attributes = True
