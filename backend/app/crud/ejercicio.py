from sqlalchemy.orm import Session
from backend.app.models.ejercicio import Ejercicio
from backend.app.schemas.ejercicio import EjercicioCreate, EjercicioUpdate

def get_ejercicio(db: Session, ejercicio_id: int):
    return db.query(Ejercicio).filter(Ejercicio.id_ejercicio==ejercicio_id).first()

def get_ejercicios(db: Session, skip: int=0, limit: int=100):
    return db.query(Ejercicio).offset(skip).limit(limit).all()

def create_ejercicio(db: Session, data: EjercicioCreate):
    obj = Ejercicio(nombre=data.nombre, descripcion=data.descripcion, grupo_muscular=data.grupo_muscular)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update_ejercicio(db: Session, db_obj, updates: EjercicioUpdate):
    for k,v in updates.dict(exclude_unset=True).items():
        setattr(db_obj, k, v)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_ejercicio(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()
