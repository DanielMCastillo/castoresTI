
CREATE TABLE roles(
	idRol INT PRIMARY KEY,
	nombre VARCHAR(50) NOT NULL
);


CREATE TABLE usuarios (
    idUsuario INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(50)  UNIQUE NOT NULL,
    contraeña VARCHAR(50) NOT NULL,
    idRol INT NOT NULL,
    FOREIGN KEY(idRol) REFERENCES roles(idRol)
);




CREATE TABLE Productos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    cantidad INT DEFAULT 0,
    estatus ENUM('activo', 'inactivo') DEFAULT 'activo'
);



CREATE TABLE Movimientos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    producto_id INT NOT NULL,
    usuario_id INT NOT NULL,
    tipo ENUM('entrada', 'salida') NOT NULL,
    cantidad INT NOT NULL,
    fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (producto_id) REFERENCES Productos(id),
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id)
);