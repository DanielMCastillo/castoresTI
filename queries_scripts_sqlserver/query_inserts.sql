USE [CastoresTI]
GO

INSERT INTO productos (idProducto, nombre, precio)
VALUES 
    (1, 'LAPTOP', 3000.00),
    (2, 'PC', 4000.00),
    (3, 'MOUSE', 100.00),
    (4, 'TECLADO', 150.00),
    (5, 'MONITOR', 2000.00),
    (6, 'MICROFONO', 350.00),
    (7, 'AUDIFONOS', 450.00);


INSERT INTO ventas(idVenta,idProducto, cantidad)
	VALUES
	 (1, 5, 8),
    (2, 1, 15),
    (3, 6, 13),
    (4, 6,4),
    (5, 2, 3),
    (6, 5, 1),
    (7, 4, 1),
	(8,2, 5),
	(9, 6, 2),
	(10, 1, 8);





GO


