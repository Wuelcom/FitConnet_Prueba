from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Logro(Base):
    __tablename__ = "logros"
    id_logro = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255), nullable=False)
    tipo = Column(String(50), nullable=False)
    puntos = Column(Integer, default=10)
