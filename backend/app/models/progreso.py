from sqlalchemy import Column, Integer, DECIMAL, DateTime, Text, ForeignKey, func
from sqlalchemy.orm import relationship
from backend.app.db.base import Base

class ProgresoUsuario(Base):
    __tablename__ = "progreso_usuario"
    id_progreso = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    peso_actual = Column(DECIMAL(5,2))
    grasa_corporal = Column(DECIMAL(5,2))
    masa_muscular = Column(DECIMAL(5,2))
    fecha_registro = Column(DateTime, server_default=func.now())
    observaciones = Column(Text)
