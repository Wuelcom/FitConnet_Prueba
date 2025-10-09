from fastapi import FastAPI
from app.db.base import Base
from app.database import engine
from fastapi.staticfiles import StaticFiles

# Aquí renombras el router correctamente
from app.auth.auth_router import router as auth_router
from app.routers import usuarios, ejercicios, rutinas, dietas, logros, progreso

app = FastAPI(title='FitConnet API')

from fastapi.middleware.cors import CORSMiddleware

# CORS for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

# app.mount('/static', StaticFiles(directory='frontend_static'), name='static')

# 🔧 Quitamos el ".router" porque ya son APIRouter directamente
app.include_router(auth_router, prefix='/api/auth', tags=['auth'])
app.include_router(usuarios.router, prefix='/api/usuarios', tags=['usuarios'])
app.include_router(ejercicios.router, prefix='/api/ejercicios', tags=['ejercicios'])
app.include_router(rutinas.router, prefix='/api/rutinas', tags=['rutinas'])
app.include_router(dietas.router, prefix='/api/dietas', tags=['dietas'])
app.include_router(logros.router, prefix='/api/logros', tags=['logros'])
app.include_router(progreso.router, prefix='/api/progreso', tags=['progreso'])
app.include_router(auth_router, prefix='/api/auth', tags=['auth'])

@app.get('/')
def root():
    return {'message': 'FitConnet API running. Open /static/index.html'}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
