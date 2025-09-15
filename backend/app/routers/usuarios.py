from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.schemas.user import UserCreate, UserOut, UserUpdate
from backend.app.crud.user import get_user, get_user_by_email, get_users, create_user, update_user, delete_user
from backend.app.database import get_db
from backend.app.auth.jwt_handler import verify_token
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(prefix='', tags=['usuarios'])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/auth/login')

@router.post('/', response_model=UserOut)
def create_user_endpoint(user_in: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_email(db, user_in.correo_electronico):
        raise HTTPException(status_code=400, detail='Correo ya registrado')
    return create_user(db, user_in)

@router.get('/', response_model=list[UserOut])
def list_users(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return get_users(db, skip=skip, limit=limit)

@router.get('/{user_id}', response_model=UserOut)
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    u = get_user(db, user_id)
    if not u:
        raise HTTPException(status_code=404, detail='Usuario no encontrado')
    return u

@router.put('/{user_id}', response_model=UserOut)
def update_user_endpoint(user_id: int, updates: UserUpdate, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail='Usuario no encontrado')
    return update_user(db, db_user, updates)

@router.delete('/{user_id}')
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail='Usuario no encontrado')
    delete_user(db, db_user)
    return {'detail':'Usuario eliminado'}

@router.get('/me')
def read_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail='Token inválido')
    email = payload.get('sub')
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail='Usuario no encontrado')
    return {'nombre': user.nombre, 'correo_electronico': user.correo_electronico, 'id_usuario': user.id_usuario}
