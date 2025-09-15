from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.progreso import ProgresoCreate, ProgresoOut
from app.crud.progreso import get_progreso, get_progresos, create_progreso, delete_progreso
from app.database import get_db

router = APIRouter(prefix='', tags=['progreso'])

@router.post('/', response_model=ProgresoOut)
def create_progreso_endpoint(p: ProgresoCreate, db: Session = Depends(get_db)):
    return create_progreso(db, p)

@router.get('/', response_model=list[ProgresoOut])
def list_progreso(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    return get_progresos(db, skip, limit)

@router.get('/{id_progreso}', response_model=ProgresoOut)
def get_progreso_endpoint(id_progreso: int, db: Session = Depends(get_db)):
    obj = get_progreso(db, id_progreso)
    if not obj:
        raise HTTPException(status_code=404, detail='Progreso no encontrado')
    return obj

@router.delete('/{id_progreso}')
def delete_progreso_endpoint(id_progreso: int, db: Session = Depends(get_db)):
    obj = get_progreso(db, id_progreso)
    if not obj:
        raise HTTPException(status_code=404, detail='Progreso no encontrado')
    delete_progreso(db, obj)
    return {'detail':'Progreso eliminado'}
