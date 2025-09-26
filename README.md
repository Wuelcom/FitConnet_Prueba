# FitConnet API - Guía de Instalación y Ejecución para Principiantes

¡Bienvenido a FitConnet! Este es un proyecto de API backend desarrollado con **FastAPI** en Python, diseñado para una aplicación de fitness y conexión. Incluye funcionalidades para gestión de usuarios, rutinas de ejercicio, dietas, logros, progreso y más. El frontend es estático (HTML/CSS/JS) servido directamente por la API.

Esta guía está escrita paso a paso para **principiantes absolutos**. Usaremos **Git Bash** como terminal (recomendado en Windows para comandos estilo Unix). Si no lo tienes, descárgalo desde [git-scm.com](https://git-scm.com/downloads).

Asumimos que estás empezando **desde cero** en una máquina nueva. El proyecto usa **MySQL** como base de datos, **SQLAlchemy** para ORM y **Alembic** para migraciones. La API corre en el puerto 8000 por defecto.

## 📋 Prerrequisitos (Instala esto primero)

Antes de empezar, asegúrate de tener instalado:

1. **Python 3.10 a 3.12** (evita 3.13 por incompatibilidades con SQLAlchemy):
   - Descarga desde [python.org](https://www.python.org/downloads/).
   - Durante la instalación, marca "Add Python to PATH".
   - Verifica en Git Bash: `python --version`. Debe mostrar algo como "Python 3.10.x" o "3.12.x".

2. **Git** (incluye Git Bash):
   - Descarga desde [git-scm.com](https://git-scm.com/downloads).
   - Instala con opciones predeterminadas.
   - Verifica: `git --version`.

3. **MySQL Server** (para la base de datos):
   - **Opción 1: XAMPP (recomendado si ya lo tienes, ya que tu proyecto está en htdocs)**:
     - Inicia XAMPP y activa "MySQL" desde el panel de control.
     - Accede a phpMyAdmin en http://localhost/phpmyadmin (usuario: root, sin contraseña por defecto).
   - **Opción 2: MySQL Standalone**:
     - Descarga MySQL Community Server desde [dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/).
     - Instala y configura un usuario root con contraseña (ej: 'rootpassword').
     - Inicia el servicio MySQL (en Windows, usa Services).
   - **Cliente MySQL**: Si necesitas el comando `mysql` en Git Bash, instala MySQL Shell o agrega MySQL bin a PATH. Alternativamente, usa MySQL Workbench (GUI) o phpMyAdmin para crear la DB.
   - Verifica: Asegúrate de que MySQL esté corriendo (puerto 3306).

4. **Git Bash**:
   - Viene con Git. Ábrelo buscando "Git Bash" en el menú de inicio.

5. **Editor de código (opcional pero recomendado)**:
   - Usa VS Code: [code.visualstudio.com](https://code.visualstudio.com/).

**Tiempo estimado para prerrequisitos: 15-30 minutos.**

## 🚀 Paso 1: Clonar o Copiar el Proyecto

Si el proyecto está en un repositorio Git remoto (ej: GitHub), clónalo. Si ya lo tienes localmente (como en tu caso, en `c:/xampp1/htdocs/FitConnet_Prueba_Corregido_Funcional`), salta al Paso 2.

Abre **Git Bash** y ejecuta:

```bash
# Navega a la carpeta donde quieres el proyecto (ej: htdocs en XAMPP)
cd /c/xampp1/htdocs

# Clona el repositorio (reemplaza <URL_REPO> con la URL real, ej: https://github.com/tuusuario/FitConnet.git)
git clone <URL_REPO> FitConnet_Prueba_Corregido_Funcional

# Entra al directorio
cd FitConnet_Prueba_Corregido_Funcional
```

Si no hay repo remoto, simplemente copia la carpeta del proyecto a tu ubicación deseada.

**Verifica**: Ejecuta `ls` en Git Bash. Debes ver carpetas como `backend/`, `alembic/`, etc.

## 🐍 Paso 2: Configurar Entorno Virtual (Virtual Environment)

Es una buena práctica aislar las dependencias del proyecto.

En Git Bash, desde la raíz del proyecto (`FitConnet_Prueba_Corregido_Funcional`):

```bash
# Crea el entorno virtual en la carpeta backend
cd backend
python -m venv venv

# Activa el entorno (en Windows/Git Bash)
source venv/Scripts/activate  # O en CMD: venv\Scripts\activate

# Verifica: Debe mostrar (venv) al inicio de la línea en Git Bash
```

**Nota**: Cada vez que abras una nueva terminal, reactiva con `source venv/Scripts/activate`.

## 📦 Paso 3: Instalar Dependencias

Con el venv activado, instala las librerías necesarias:

```bash
# Desde backend/
pip install -r requirements.txt
```

Esto instalará:
- `fastapi`: Framework para la API.
- `uvicorn[standard]`: Servidor ASGI para correr FastAPI.
- `SQLAlchemy==2.0.31`: ORM para base de datos (compatible con Python 3.13).
- `pymysql`: Driver para MySQL.
- `alembic`: Para migraciones de DB.
- `python-dotenv`: Para variables de entorno.
- `passlib[bcrypt]`: Para hashing de contraseñas.
- `python-jose[cryptography]`: Para JWT (autenticación).
- `pydantic`: Validación de datos.
- `email-validator`: Validación de emails.

**Tiempo estimado: 2-5 minutos.** Si hay errores (ej: pip no encontrado), reinstala Python con "Add to PATH".

**Verifica**: Ejecuta `pip list`. Debe mostrar las dependencias instaladas.

## 🗄️ Paso 4: Configurar la Base de Datos

El proyecto usa **MySQL**. Necesitas crear una base de datos y configurar las credenciales.

1. **Instala y configura MySQL** (si no lo has hecho):
   - Usa XAMPP (ya que tu directorio es en htdocs): Inicia Apache y MySQL desde el panel de XAMPP.
   - O instala MySQL standalone.

2. **Crea la base de datos**:
   - **Usando phpMyAdmin (XAMPP)**:
     - Ve a http://localhost/phpmyadmin.
     - Inicia sesión (usuario: root, contraseña: vacía por defecto).
     - Crea una nueva base de datos llamada `FitConnet` (collation: utf8mb4_unicode_ci).
   - **Usando MySQL Workbench**:
     - Abre MySQL Workbench, conecta a localhost.
     - Ejecuta: `CREATE DATABASE FitConnet CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;`
   - **Usando terminal MySQL** (si tienes el cliente instalado):
     ```bash
     # En Git Bash o CMD, conecta a MySQL (ajusta user/pass)
     mysql -u root -p
     ```
     ```sql
     -- Crea la DB (nombre: FitConnet, ajusta si quieres)
     CREATE DATABASE FitConnet CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
     EXIT;
     ```
   - **Nota**: Si no tienes contraseña en XAMPP, usa `mysql+pymysql://root:@localhost/FitConnet` en .env (sin contraseña). El nombre por defecto es "FitConnet".

3. **Configura variables de entorno**:
   - Crea un archivo `.env` en la raíz del proyecto (o en `backend/`, ajusta config.py si es necesario).
   - Contenido de `.env` (reemplaza con tus valores):
     ```
     DATABASE_URL=mysql+pymysql://root:tu_contraseña@localhost/FitConnet
     SECRET_KEY=tu_clave_secreta_super_segura_aqui  # Genera una con: openssl rand -hex 32
     ALGORITHM=HS256
     ACCESS_TOKEN_EXPIRE_MINUTES=30
     ```

   - En `backend/app/config.py`, asegúrate de que cargue el .env:
     (Si no existe, agrégalo; basado en el código, usa python-dotenv).

**Verifica conexión**: En Python (con venv activado):
```bash
cd backend
python
```
```python
from app.database import engine
engine.connect()  # No debe dar error
exit()
```

## 🔄 Paso 5: Ejecutar Migraciones de Base de Datos

Usa Alembic para crear las tablas.

Desde la raíz del proyecto (con venv activado):

```bash
# Inicializa Alembic si no está (ya existe alembic.ini)
cd backend  # Si no estás ahí

# Estampilla inicial (si es la primera vez)
alembic stamp head

# Aplica migraciones (crea tablas de models como User, Rutina, etc.)
alembic upgrade head
```

**Nota**: Si hay errores, revisa `alembic.ini` y asegúrate de que `sqlalchemy.url` apunte a tu DATABASE_URL.

**Verifica**: Conecta a MySQL y ejecuta `SHOW TABLES;`. Debes ver tablas como `users`, `rutinas`, etc.

## ⚡ Paso 6: Correr el Servidor FastAPI

Con venv activado, desde `backend/`:

```bash
# Opción 1: Usando uvicorn directamente (recomendado para desarrollo)
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload

# Opción 2: Usando el script en main.py
python app/main.py
```

- `--reload`: Recarga automáticamente al cambiar código.
- Si el puerto 8000 está ocupado, cambia a `--port 8001`.

**Verifica**: Debe mostrar algo como "Uvicorn running on http://127.0.0.1:8000".

**Tiempo estimado: El servidor arranca en segundos.**

## 🌐 Paso 7: Acceder a la API y Frontend

Abre tu navegador (Chrome/Firefox) y ve a:

1. **API Principal**: http://127.0.0.1:8000/
   - Respuesta: `{'message': 'FitConnet API running. Open /static/index.html'}`

2. **Documentación Interactiva (Swagger UI)**: http://127.0.0.1:8000/docs
   - Aquí ves **todas las funciones/endpoints** con descripciones, pruebas y código de ejemplo.
   - Usa el botón "Try it out" para probar requests (necesitas auth para algunos).

3. **Frontend Estático**: http://127.0.0.1:8000/static/index.html
   - Página principal de la app (login, register, etc.).
   - CSS/JS en `/static/css/` y `/static/js/`.
   - Imágenes en `/static/img/`.

4. **ReDoc (alternativa a Swagger)**: http://127.0.0.1:8000/redoc

**Nota**: El frontend es básico y estático; interactúa con la API via JS (ver `login.js`, `register.js`).

## 🔍 Funciones y Endpoints (Cada Ruta Principal)

La API está organizada en **routers** (módulos). Cada uno maneja CRUD (Crear, Leer, Actualizar, Eliminar) para entidades de fitness. Usa **JWT para autenticación** (regístrate/login primero).

Ve a `/docs` para detalles completos, pero aquí un resumen:

### 1. **Autenticación (/api/auth)**
   - `POST /api/auth/register`: Registra un nuevo usuario (nombre, email, contraseña). Retorna JWT token.
   - `POST /api/auth/login`: Inicia sesión (email, contraseña). Retorna JWT token.
   - `GET /api/auth/me`: Obtiene datos del usuario logueado (requiere token en headers: Authorization: Bearer <token>).
   - **Uso**: Tokens expiran en 30 min. Usa para proteger otras rutas.

### 2. **Usuarios (/api/usuarios)**
   - `GET /api/usuarios/`: Lista todos los usuarios (admin solo?).
   - `GET /api/usuarios/{id}`: Detalles de un usuario.
   - `POST /api/usuarios/`: Crea usuario (similar a register).
   - `PUT /api/usuarios/{id}`: Actualiza usuario (perfil, rol).
   - `DELETE /api/usuarios/{id}`: Elimina usuario.
   - **Modelos**: User con rol (user/admin), email validado.

### 3. **Ejercicios (/api/ejercicios)**
   - `GET /api/ejercicios/`: Lista ejercicios (ej: sentadillas, flexiones).
   - `GET /api/ejercicios/{id}`: Detalles de un ejercicio.
   - `POST /api/ejercicios/`: Crea nuevo ejercicio (nombre, descripción, músculos).
   - `PUT /api/ejercicios/{id}`: Actualiza.
   - `DELETE /api/ejercicios/{id}`: Elimina.
   - **Uso**: Para rutinas personalizadas.

### 4. **Rutinas (/api/rutinas)**
   - `GET /api/rutinas/`: Lista rutinas de usuario.
   - `GET /api/rutinas/{id}`: Detalles (incluye ejercicios).
   - `POST /api/rutinas/`: Crea rutina (nombre, duración, ejercicios).
   - `PUT /api/rutinas/{id}`: Actualiza progreso.
   - `DELETE /api/rutinas/{id}`: Elimina.
   - **Modelos**: Rutina vinculada a User y Ejercicio.

### 5. **Dietas (/api/dietas)**
   - Similar a rutinas: CRUD para planes de dieta (comidas, calorías, nutrientes).
   - `GET /api/dietas/`: Lista dietas.
   - `POST /api/dietas/`: Crea dieta personalizada.

### 6. **Logros (/api/logros)**
   - `GET /api/logros/`: Lista logros desbloqueados (ej: "Completaste 10 workouts").
   - `POST /api/logros/`: Asigna logro a usuario.
   - Vinculados a progreso/rutinas.

### 7. **Progreso (/api/progreso)**
   - `GET /api/progreso/`: Rastrea avances (peso, reps, etc.).
   - `POST /api/progreso/`: Registra entrada de progreso.
   - `PUT /api/progreso/{id}`: Actualiza.

**Autenticación Requerida**: La mayoría de endpoints (excepto register/login) necesitan JWT en headers. En `/docs`, agrega el token en "Authorize".

**Ejemplo de Request (usando curl en Git Bash)**:
```bash
# Login
curl -X POST "http://127.0.0.1:8000/api/auth/login" -H "Content-Type: application/json" -d '{"email":"test@example.com","password":"password"}'

# Usa el token retornado para otros calls
curl -X GET "http://127.0.0.1:8000/api/usuarios/" -H "Authorization: Bearer TU_TOKEN_AQUI"
```

## 🛠️ Pasos Adicionales y Mejoras

- **Variables de Entorno**: Edita `.env` para producción (cambia SECRET_KEY, DB URL). Nunca commitees .env a Git (agrega a .gitignore si no está).

- **Migraciones Personalizadas**:
  - Para cambios en models (ej: agregar campo): `alembic revision --autogenerate -m "Descripción"`, luego `alembic upgrade head`.

- **Frontend Avanzado**: El actual es estático. Para desarrollo, abre `index.html` en VS Code Live Server. JS hace fetch a la API.

- **Pruebas**:
  - Regístrate via `/docs` o frontend.
  - Crea una rutina y progreso.
  - Verifica en DB: `SELECT * FROM users;` en MySQL.

- **Desarrollo**:
  - Edita código en `backend/app/routers/` para agregar features.
  - Usa VS Code con extensión Python para debugging.

## ❌ Solución de Problemas Comunes

- **Error: "No module named 'app'"**: Asegúrate de estar en `backend/` y venv activado.
- **Error DB: "Can't connect to MySQL"**: Verifica MySQL corriendo, credenciales en .env, puerto 3306 libre.
- **Puerto 8000 ocupado**: Cambia a `--port 8001` y actualiza URLs.
- **Migraciones fallan**: Borra DB y recrea, o `alembic downgrade base` y re-upgrade.
- **JWT inválido**: Verifica SECRET_KEY y expiración.
- **Windows/Git Bash issues**: Usa `winpty python` si hay problemas con venv.
- **Dependencias no instalan**: Actualiza pip: `pip install --upgrade pip`.
- **AssertionError con SQLAlchemy en Python 3.13**: SQLAlchemy 2.0.19 no es compatible con Python 3.13. Usa Python 3.10-3.12, o actualiza requirements.txt a SQLAlchemy==2.0.31 si usas 3.13 (luego reinstala dependencias: `rm -rf venv && python -m venv venv && source venv/Scripts/activate && pip install -r requirements.txt`).

Si algo falla, copia el error y busca en Google/Stack Overflow, o pregunta en foros como Reddit r/learnpython.

## 📝 Contribuciones

- Edita routers/models en `backend/app/`.
- Agrega tests en el futuro (usa pytest).
- Commitea cambios: `git add . && git commit -m "Mensaje" && git push`.

¡Felicidades! Ahora tienes FitConnet corriendo. Explora `/docs` para probar todo. Si necesitas más ayuda, revisa el código o contacta al desarrollador.

**Versión del Proyecto**: Basado en FastAPI + SQLAlchemy. Última actualización: [Fecha actual].
