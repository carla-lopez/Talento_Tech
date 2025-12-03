CREATE DATABASE IF NOT EXISTS almacen_db;

USE almacen_db;

CREATE TABLE IF NOT EXISTS productos (
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR (100) NOT NULL,
categoria VARCHAR (50) NOT NULL,
precio INT NOT NULL
);

INSERT INTO productos (nombre,categoria,precio) VALUES ('Producto Prueba', 'General',100);

SELECT * FROM productos;

