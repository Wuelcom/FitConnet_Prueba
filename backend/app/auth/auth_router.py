from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.user import get_user_by_email, create_user
from app.schemas.user import UserCreate, UserOut
from app.auth.security import verify_password
from app.auth.jwt_handler import create_access_token

router = APIRouter(prefix='/auth', tags=['auth'])

@router.post('/register', response_model=UserOut)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_email(db, user_in.correo_electronico):
        raise HTTPException(status_code=400, detail='Correo ya registrado')
    return create_user(db, user_in)

@router.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.contrasena):
        raise HTTPException(status_code=401, detail='Credenciales inválidas')
    token = create_access_token({'sub': user.correo_electronico})
    return {'access_token': token, 'token_type': 'bearer'}
