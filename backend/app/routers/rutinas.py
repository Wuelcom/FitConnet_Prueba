from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.rutina import RutinaCreate, RutinaOut, RutinaUpdate
from app.crud.rutina import get_rutina, get_rutinas, create_rutina, update_rutina, delete_rutina
from app.database import get_db

router = APIRouter(prefix='', tags=['rutinas'])

@router.post('/', response_model=RutinaOut)
def create_rutina_endpoint(r: RutinaCreate, db: Session = Depends(get_db)):
    return create_rutina(db, r)

@router.get('/', response_model=list[RutinaOut])
def list_rutinas(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    return get_rutinas(db, skip, limit)

@router.get('/{id_rutina}', response_model=RutinaOut)
def get_rutina_endpoint(id_rutina: int, db: Session = Depends(get_db)):
    obj = get_rutina(db, id_rutina)
    if not obj:
        raise HTTPException(status_code=404, detail='Rutina no encontrada')
    return obj

@router.put('/{id_rutina}', response_model=RutinaOut)
def update_rutina_endpoint(id_rutina: int, updates: RutinaUpdate, db: Session = Depends(get_db)):
    obj = get_rutina(db, id_rutina)
    if not obj:
        raise HTTPException(status_code=404, detail='Rutina no encontrada')
    return update_rutina(db, obj, updates)

@router.delete('/{id_rutina}')
def delete_rutina_endpoint(id_rutina: int, db: Session = Depends(get_db)):
    obj = get_rutina(db, id_rutina)
    if not obj:
        raise HTTPException(status_code=404, detail='Rutina no encontrada')
    delete_rutina(db, obj)
    return {'detail':'Rutina eliminada'}
