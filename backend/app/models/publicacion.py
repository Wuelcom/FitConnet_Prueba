from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey, func
from backend.app.db.base import Base

class Publicacion(Base):
    __tablename__ = "publicaciones"
    id_publicacion = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    contenido = Column(Text, nullable=False)
    fecha_publicacion = Column(DateTime, server_default=func.now())
