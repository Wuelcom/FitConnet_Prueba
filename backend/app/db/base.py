from sqlalchemy.orm import declarative_base
Base = declarative_base()
# models imported for Alembic detection
from backend.app.models.user import Usuario
from backend.app.models.objetivo import Objetivo
from backend.app.models.role import RolUsuario
from backend.app.models.rutina import Rutina
from backend.app.models.ejercicio import Ejercicio
from backend.app.models.dieta import PlanDieta
from backend.app.models.progreso import ProgresoUsuario
from backend.app.models.publicacion import Publicacion
from backend.app.models.logro import Logro
