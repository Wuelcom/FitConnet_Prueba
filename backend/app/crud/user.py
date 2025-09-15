from sqlalchemy.orm import Session
from backend.app.models.user import Usuario
from backend.app.schemas.user import UserCreate, UserUpdate
from backend.app.auth.security import get_password_hash

def get_user(db: Session, user_id: int):
    return db.query(Usuario).filter(Usuario.id_usuario == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.correo_electronico == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Usuario).offset(skip).limit(limit).all()

def create_user(db: Session, user_in: UserCreate):
    hashed = get_password_hash(user_in.contrasena)
    db_user = Usuario(
        nombre=user_in.nombre,
        correo_electronico=user_in.correo_electronico,
        contrasena=hashed,
        fecha_nacimiento=user_in.fecha_nacimiento,
        telefono=user_in.telefono,
        id_objetivo=user_in.id_objetivo
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, db_user, updates: UserUpdate):
    for k, v in updates.dict(exclude_unset=True).items():
        setattr(db_user, k, v)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, db_user):
    db.delete(db_user)
    db.commit()
