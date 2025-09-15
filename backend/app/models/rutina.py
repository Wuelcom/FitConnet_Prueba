from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from backend.app.db.base import Base

class Rutina(Base):
    __tablename__ = "rutinas"
    id_rutina = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    id_objetivo = Column(Integer, ForeignKey("objetivos.id_objetivo"))
    nombre_rutina = Column(String(100), nullable=False)
    descripcion = Column(Text)
    fecha_creacion = Column(DateTime, server_default=func.now())
