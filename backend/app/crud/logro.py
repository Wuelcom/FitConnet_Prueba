from sqlalchemy.orm import Session
from app.models.logro import Logro
from app.schemas.logro import LogroCreate

def get_logro(db: Session, id_logro: int):
    return db.query(Logro).filter(Logro.id_logro==id_logro).first()

def get_logros(db: Session, skip: int=0, limit: int=100):
    return db.query(Logro).offset(skip).limit(limit).all()

def create_logro(db: Session, data: LogroCreate):
    obj = Logro(nombre=data.nombre, descripcion=data.descripcion, tipo=data.tipo, puntos=data.puntos)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def delete_logro(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()
