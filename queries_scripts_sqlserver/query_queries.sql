SELECT * FROM productos;
SELECT * FROM ventas;


 

SELECT DISTINCT p.idProducto, p.nombre, p.precio 
FROM productos p 
JOIN ventas v ON p.idProducto = v.idProducto; 


SELECT p.idProducto, p.nombre, p.precio, SUM(v.cantidad) AS totalVentas
FROM productos p
JOIN ventas v ON p.idProducto = v.idProducto
GROUP BY p.idProducto, p.nombre, p.precio;


SELECT p.idProducto, p.nombre, p.precio, 
       COALESCE(SUM(v.cantidad * CAST(p.precio AS DECIMAL(10,2))), 0) AS totalVentas
FROM productos p
LEFT JOIN ventas v ON p.idProducto = v.idProducto
GROUP BY p.idProducto, p.nombre, p.precio;
