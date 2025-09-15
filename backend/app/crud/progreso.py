from sqlalchemy.orm import Session
from app.models.progreso import ProgresoUsuario
from app.schemas.progreso import ProgresoCreate

def get_progreso(db: Session, id_progress: int):
    return db.query(ProgresoUsuario).filter(ProgresoUsuario.id_progreso==id_progress).first()

def get_progresos(db: Session, skip:int=0, limit:int=100):
    return db.query(ProgresoUsuario).offset(skip).limit(limit).all()

def create_progreso(db: Session, data: ProgresoCreate):
    obj = ProgresoUsuario(id_usuario=data.id_usuario, peso_actual=data.peso_actual, grasa_corporal=data.grasa_corporal, masa_muscular=data.masa_muscular, observaciones=data.observaciones)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def delete_progreso(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()
