from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.schemas.dieta import DietaCreate, DietaOut
from backend.app.crud.dieta import get_dieta, get_dietas, create_dieta, delete_dieta
from backend.app.database import get_db

router = APIRouter(prefix='', tags=['dietas'])

@router.post('/', response_model=DietaOut)
def create_dieta_endpoint(d: DietaCreate, db: Session = Depends(get_db)):
    return create_dieta(db, d)

@router.get('/', response_model=list[DietaOut])
def list_dietas(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    return get_dietas(db, skip, limit)

@router.get('/{id_dieta}', response_model=DietaOut)
def get_dieta_endpoint(id_dieta: int, db: Session = Depends(get_db)):
    obj = get_dieta(db, id_dieta)
    if not obj:
        raise HTTPException(status_code=404, detail='Dieta no encontrada')
    return obj

@router.delete('/{id_dieta}')
def delete_dieta_endpoint(id_dieta: int, db: Session = Depends(get_db)):
    obj = get_dieta(db, id_dieta)
    if not obj:
        raise HTTPException(status_code=404, detail='Dieta no encontrada')
    delete_dieta(db, obj)
    return {'detail':'Dieta eliminada'}
