from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey, func
from sqlalchemy.orm import relationship
from app.db.base import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    correo_electronico = Column(String(100), unique=True, nullable=False, index=True)
    contrasena = Column(String(255), nullable=False)
    fecha_registro = Column(DateTime, server_default=func.now())
    fecha_nacimiento = Column(Date, nullable=True)
    telefono = Column(String(20), nullable=True)
    id_objetivo = Column(Integer, ForeignKey("objetivos.id_objetivo"), nullable=True)

    objetivo = relationship("Objetivo", back_populates="usuarios")
