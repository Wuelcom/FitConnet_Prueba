from fastapi import FastAPI
from backend.app.db.base import Base
from backend.app.database import engine
from fastapi.staticfiles import StaticFiles

from backend.app.auth import auth_router
from backend.app.routers import usuarios, ejercicios, rutinas, dietas, logros, progreso

app = FastAPI(title='FitConnet API')

Base.metadata.create_all(bind=engine)



app.mount('/static', StaticFiles(directory='backend/frontend_static'), name='static')

app.include_router(auth_router.router, prefix='/api/auth', tags=['auth'])
app.include_router(usuarios.router, prefix='/api/usuarios', tags=['usuarios'])
app.include_router(ejercicios.router, prefix='/api/ejercicios', tags=['ejercicios'])
app.include_router(rutinas.router, prefix='/api/rutinas', tags=['rutinas'])
app.include_router(dietas.router, prefix='/api/dietas', tags=['dietas'])
app.include_router(logros.router, prefix='/api/logros', tags=['logros'])
app.include_router(progreso.router, prefix='/api/progreso', tags=['progreso'])

@app.get('/')
def root():
    return {'message':'FitConnet API running. Open /static/index.html'}
