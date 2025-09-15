from sqlalchemy import Column, Integer, String
from app.db.base import Base

class RolUsuario(Base):
    __tablename__ = "rol_usuarios"
    id_rol = Column(Integer, primary_key=True, index=True)
    rol = Column(String(50), nullable=False)
