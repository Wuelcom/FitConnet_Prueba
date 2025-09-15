from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.schemas.ejercicio import EjercicioCreate, EjercicioOut, EjercicioUpdate
from backend.app.crud.ejercicio import get_ejercicio, get_ejercicios, create_ejercicio, update_ejercicio, delete_ejercicio
from backend.app.database import get_db

router = APIRouter(prefix='', tags=['ejercicios'])

@router.post('/', response_model=EjercicioOut)
def create_ejercicio_endpoint(e: EjercicioCreate, db: Session = Depends(get_db)):
    return create_ejercicio(db, e)

@router.get('/', response_model=list[EjercicioOut])
def list_ejercicios(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    return get_ejercicios(db, skip, limit)

@router.get('/{ejercicio_id}', response_model=EjercicioOut)
def get_ejercicio_endpoint(ejercicio_id: int, db: Session = Depends(get_db)):
    obj = get_ejercicio(db, ejercicio_id)
    if not obj:
        raise HTTPException(status_code=404, detail='Ejercicio no encontrado')
    return obj

@router.put('/{ejercicio_id}', response_model=EjercicioOut)
def update_ej_endpoint(ejercicio_id: int, updates: EjercicioUpdate, db: Session = Depends(get_db)):
    obj = get_ejercicio(db, ejercicio_id)
    if not obj:
        raise HTTPException(status_code=404, detail='Ejercicio no encontrado')
    return update_ejercicio(db, obj, updates)

@router.delete('/{ejercicio_id}')
def delete_ej_endpoint(ejercicio_id: int, db: Session = Depends(get_db)):
    obj = get_ejercicio(db, ejercicio_id)
    if not obj:
        raise HTTPException(status_code=404, detail='Ejercicio no encontrado')
    delete_ejercicio(db, obj)
    return {'detail':'Ejercicio eliminado'}
