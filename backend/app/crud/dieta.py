from sqlalchemy.orm import Session
from app.models.dieta import PlanDieta
from app.schemas.dieta import DietaCreate

def get_dieta(db: Session, id_dieta: int):
    return db.query(PlanDieta).filter(PlanDieta.id_dieta==id_dieta).first()

def get_dietas(db: Session, skip: int=0, limit: int=100):
    return db.query(PlanDieta).offset(skip).limit(limit).all()

def create_dieta(db: Session, data: DietaCreate):
    obj = PlanDieta(nombre_dieta=data.nombre_dieta, descripcion=data.descripcion, funcion_dieta=data.funcion_dieta)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def delete_dieta(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()
