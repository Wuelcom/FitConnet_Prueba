from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.logro import LogroCreate, LogroOut
from app.crud.logro import get_logro, get_logros, create_logro, delete_logro
from app.database import get_db

router = APIRouter(prefix='', tags=['logros'])

@router.post('/', response_model=LogroOut)
def create_logro_endpoint(l: LogroCreate, db: Session = Depends(get_db)):
    return create_logro(db, l)

@router.get('/', response_model=list[LogroOut])
def list_logros(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    return get_logros(db, skip, limit)

@router.get('/{id_logro}', response_model=LogroOut)
def get_logro_endpoint(id_logro: int, db: Session = Depends(get_db)):
    obj = get_logro(db, id_logro)
    if not obj:
        raise HTTPException(status_code=404, detail='Logro no encontrado')
    return obj

@router.delete('/{id_logro}')
def delete_logro_endpoint(id_logro: int, db: Session = Depends(get_db)):
    obj = get_logro(db, id_logro)
    if not obj:
        raise HTTPException(status_code=404, detail='Logro no encontrado')
    delete_logro(db, obj)
    return {'detail':'Logro eliminado'}
