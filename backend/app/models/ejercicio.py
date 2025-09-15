from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db.base import Base

class Ejercicio(Base):
    __tablename__ = "ejercicios"
    id_ejercicio = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    grupo_muscular = Column(String(50))
