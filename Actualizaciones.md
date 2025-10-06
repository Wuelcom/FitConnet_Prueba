nueva base de datos: 

-- CREACIÓN DE BASE DE DATOS
DROP DATABASE IF EXISTS FitConnet;
CREATE DATABASE FitConnet;
USE FitConnet;

-- TABLA USUARIOS
CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    edad INT,
    peso DECIMAL(5,2),
    altura DECIMAL(5,2),
    genero ENUM('M','F','Otro'),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- TABLA ROLES
CREATE TABLE roles (
    id_rol INT AUTO_INCREMENT PRIMARY KEY,
    nombre_rol VARCHAR(50) NOT NULL
);

-- TABLA ASIGNACIÓN DE ROLES
CREATE TABLE usuario_rol (
    id_usuario INT,
    id_rol INT,
    PRIMARY KEY (id_usuario, id_rol),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_rol) REFERENCES roles(id_rol)
);

-- TABLA OBJETIVOS
CREATE TABLE objetivos (
    id_objetivo INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(200) NOT NULL
);

-- TABLA RUTINAS
CREATE TABLE rutinas (
    id_rutina INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    nivel ENUM('Principiante','Intermedio','Avanzado'),
    duracion INT COMMENT 'Duración en minutos',
    id_usuario INT,
    id_objetivo INT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_objetivo) REFERENCES objetivos(id_objetivo)
);

-- TABLA EJERCICIOS
CREATE TABLE ejercicios (
    id_ejercicio INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo ENUM('Cardio','Fuerza','Flexibilidad','Resistencia','Otro'),
    musculo_principal VARCHAR(100),
    descripcion TEXT
);

-- RELACIÓN RUTINA - EJERCICIOS
CREATE TABLE rutina_ejercicio (
    id_rutina INT,
    id_ejercicio INT,
    series INT,
    repeticiones INT,
    descanso INT COMMENT 'Segundos de descanso',
    PRIMARY KEY (id_rutina, id_ejercicio),
    FOREIGN KEY (id_rutina) REFERENCES rutinas(id_rutina),
    FOREIGN KEY (id_ejercicio) REFERENCES ejercicios(id_ejercicio)
);

-- TABLA LOGROS
CREATE TABLE logros (
    id_logro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    puntos INT DEFAULT 0
);

-- RELACIÓN USUARIO - LOGROS
CREATE TABLE usuario_logro (
    id_usuario INT,
    id_logro INT,
    fecha_obtenido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id_usuario, id_logro),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_logro) REFERENCES logros(id_logro)
);

-- TABLA PLANES DE DIETA
CREATE TABLE planes_dieta (
    id_dieta INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    objetivo VARCHAR(200) NOT NULL,
    descripcion TEXT NOT NULL
);

-- TABLA SEGUIMIENTO DE PROGRESO
CREATE TABLE progreso (
    id_progreso INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    fecha DATE NOT NULL,
    peso DECIMAL(5,2),
    grasa_corporal DECIMAL(5,2),
    musculo DECIMAL(5,2),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

-- TABLA PUBLICACIONES (tipo red social)
CREATE TABLE publicaciones (
    id_publicacion INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    contenido TEXT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

-- TABLA COMENTARIOS
CREATE TABLE comentarios (
    id_comentario INT AUTO_INCREMENT PRIMARY KEY,
    id_publicacion INT,
    id_usuario INT,
    contenido TEXT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_publicacion) REFERENCES publicaciones(id_publicacion),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

-- TABLA REACCIONES (likes, etc.)
CREATE TABLE reacciones (
    id_reaccion INT AUTO_INCREMENT PRIMARY KEY,
    id_publicacion INT,
    id_usuario INT,
    tipo ENUM('Like','Love','Clap','Star'),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_publicacion) REFERENCES publicaciones(id_publicacion),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);


------------------------------------------------------------------------------------------------------------

