from pydantic import BaseModel
from typing import Optional

class DietaBase(BaseModel):
    nombre_dieta: str
    descripcion: Optional[str] = None
    funcion_dieta: str

class DietaCreate(DietaBase):
    pass

class DietaOut(DietaBase):
    id_dieta: int
    class Config:
        from_attributes = True
