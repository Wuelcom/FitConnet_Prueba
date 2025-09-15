from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.app.db.base import Base

class Objetivo(Base):
    __tablename__ = "objetivos"
    id_objetivo = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(100), nullable=False)
    usuarios = relationship("Usuario", back_populates="objetivo")
