CREATE TABLE productos (
    idProducto INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
	precio VARCHAR(100) NOT NULL,
);

CREATE TABLE ventas (
    idVenta INT PRIMARY KEY,
    cantidad INT NOT NULL,
	idProducto INT, 
    FOREIGN KEY (idProducto) REFERENCES productos(idProducto) ON DELETE SET NULL
);
