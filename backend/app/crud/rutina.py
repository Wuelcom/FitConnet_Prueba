from sqlalchemy.orm import Session
from app.models.rutina import Rutina
from app.schemas.rutina import RutinaCreate, RutinaUpdate

def get_rutina(db: Session, id_rutina: int):
    return db.query(Rutina).filter(Rutina.id_rutina==id_rutina).first()

def get_rutinas(db: Session, skip: int=0, limit: int=100):
    return db.query(Rutina).offset(skip).limit(limit).all()

def create_rutina(db: Session, data: RutinaCreate):
    obj = Rutina(id_usuario=data.id_usuario, id_objetivo=data.id_objetivo, nombre_rutina=data.nombre_rutina, descripcion=data.descripcion)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update_rutina(db: Session, db_obj, updates: RutinaUpdate):
    for k,v in updates.dict(exclude_unset=True).items():
        setattr(db_obj,k,v)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_rutina(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()
