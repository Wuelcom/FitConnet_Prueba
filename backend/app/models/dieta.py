from sqlalchemy import Column, Integer, String, Text
from backend.app.db.base import Base

class PlanDieta(Base):
    __tablename__ = "planes_dieta"
    id_dieta = Column(Integer, primary_key=True, index=True)
    nombre_dieta = Column(String(100), nullable=False)
    descripcion = Column(Text)
    funcion_dieta = Column(String(100), nullable=False)
