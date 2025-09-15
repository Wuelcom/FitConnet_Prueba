from sqlalchemy.orm import declarative_base
Base = declarative_base()
# models imported for Alembic detection
from app.models.user import Usuario
from app.models.objetivo import Objetivo
from app.models.role import RolUsuario
from app.models.rutina import Rutina
from app.models.ejercicio import Ejercicio
from app.models.dieta import PlanDieta
from app.models.progreso import ProgresoUsuario
from app.models.publicacion import Publicacion
from app.models.logro import Logro
