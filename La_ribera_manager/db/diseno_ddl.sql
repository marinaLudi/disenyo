-- Poblamos tablas tp diseno

INSERT INTO pais (id_pais, nombre) VALUES
	(1, 'EEUU'),
	(2, 'Argentina'),
	(3, 'Rusia'),
	(4, 'Brasil'),
	(5, 'Chile'),
	(6, 'Uruguay'),
	(7, 'Paraguay'),
	(8, 'Bolivia'),
	(9, 'Peru'),
	(10, 'Canada'),
	(11, 'Mexico'),
	(12, 'Puerto Rico'),
	(13, 'Ecuador'),
	(14, 'Francia'),
	(15, 'Alemania'),
	(16, 'Espana'),
	(17, 'Portugal'),
	(18, 'Inglaterra'),
	(19, 'Holanda'),
	(20, 'Japon'),
	(21, 'China'),
	(22, 'Colombia');

INSERT INTO provincia (id_provincia, nombre, id_pais) VALUES
	(1, 'Columbia', 1),
	(2, 'Santa Fe', 2),
	(3, 'Entre Rios', 2),
	(4, 'Buenos Aires', 2),
	(5, 'Cordoba', 2),
	(6, 'Santiago del Estero', 2),
	(7, 'Leningrad', 3),
	(8, 'Yaroslavl', 3),
	(9, 'Corrientes', 2),
	(10, 'California', 1),
	(11, 'New York', 1),
	(12, 'Bahia', 4),
	(13, 'Sao Paulo', 4),
	(14, 'Rio de Janeiro', 4),
	(15, 'Santiago', 5),
	(16, 'Concepcion', 5),
	(17, 'Colonia', 6),
	(18, 'Montevideo', 6),
	(19, 'Canelones', 6),
	(20, 'Itapua', 7),
	(21, 'Concepcion', 7),
	(22, 'Potosi', 8),
	(23, 'Tarija', 8),
	(24, 'La Paz', 8),
	(25, 'Arequipa', 9),
	(26, 'Lima', 9),
	(27, 'Ontario', 10),
	(28, 'Quebec', 10),
	(29, 'Michoacan', 11),
	(30, 'Morelos', 11),
	(31, 'Ponce', 12),
	(32, 'Bolivar', 13),
	(33, 'Ile-de-France', 14),
	(34, 'Normandie', 14),
	(35, 'Lyonnais', 14),
	(36, 'Berlin', 15),
	(37, 'Bayern', 15),
	(38, 'Barcelona', 16),
	(39, 'Sevilla', 16),
	(40, 'Lisboa', 17),
	(41, 'Nottingham', 18),
	(42, 'Birmingham', 18),
	(43, 'Liverpool', 18),
	(44, 'Limburg', 19),
	(45, 'Utrecht', 19),
	(46, 'Kanto', 20),
	(47, 'Kansai', 20),
	(48, 'Beijing', 21),
	(49, 'Shanxi', 21),
	(50, 'Bajo Cauca', 22);

INSERT INTO localidad (id_localidad, nombre, id_provincia) VALUES
	(1, 'Washington', 1),
	(2, 'Santa Fe', 2),
	(3, 'Rosario', 2),
	(4, 'Rafaela', 2),
	(5, 'Parana', 3),
	(6, 'Gualeguay', 3),
	(7, 'Distrito Federal', 4),
	(8, 'La Plata', 4),
	(10, 'Cordoba', 5),
	(11, 'La Falda', 5),
	(12, 'Santiago del Estero', 6),
	(13, 'La Banda', 6),
	(14, 'San Petersburgo', 7),
	(15, 'Rostov', 8),
	(16, 'Corrientes', 9),
	(17, 'Laguna Brava', 9),
	(18, 'Los Angeles', 10),
	(19, 'San Francisco', 10),
	(20, 'San Diego', 10),
	(21, 'New York', 11),
	(22, 'Long Beach', 11),
	(23, 'Sao Paulo', 13);

INSERT INTO direccion (id_direccion, calle, numero, dpto, piso, "CP", id_localidad) VALUES
	(1, 'S.Peter', '100', 'A', 1, '10000', 1),
	(2, 'Maurice Rd.', '234', 'B', 1, '10000', 1),
	(3, 'Hernandarias', '2445', Null, Null, '3000', 2),
	(4, 'Du hast', '300', 'B', 2, '1234', 14),
	(5, 'Caipirinha', '230', Null, Null, '4400', 23);

INSERT INTO nacionalidad (id_nacionalidad, nombre) VALUES
	(1, 'Americano'),
	(2, 'Argentino'),
	(3, 'Ruso'),
	(4, 'Brasilero');

INSERT INTO ocupacion (id_ocupacion, descripcion) VALUES
	(1, 'Empleado Publico'),
	(2, 'Estudiante'),
	(3, 'Obrero'),
	(4, 'Artista');

INSERT INTO iva (id_iva, descripcion) VALUES
	(1, 'Consumidor Final'),
	(2, 'Monotributista'),
	(3, 'Exento'),
	(4, 'No Responsable');

INSERT INTO tipo_documento (id_tipo, tipo) VALUES
	(1, 'ID'),
	(2, 'DNI'),
	(3, 'RU'),
	(4, 'BRA');

INSERT INTO documento (id_documento, codigo, id_tipo) VALUES
	(1, '3013255', 1),
	(2, '3000000', 1),
	(3, '37153113', 2),
	(4, 'E1234123', 3),
	(5, 'A5434523', 3),
	(6, '54313321', 4);

INSERT INTO pasajero (id_pasajero, nombre, apellido, cuit, email, fecha_de_nac, telefono, id_documento, id_direccion, id_nacionalidad, id_ocupacion, id_iva) VALUES
	(1, 'Fox', 'Mulder', Null, 'mulder@fbi.us', '10/10/65', '469099', 1, 1, 1, 1, 1),
	(2, 'Dana', 'Scully', Null, 'scully@fbi.us', '10/11/66', '499985', 2, 2, 1, 1, 1),
	(3, 'Pablo', 'Tesari', Null,'pablotesari@gmail.com', '03/10/92', '4604340', 3, 3, 2, 2, 1),
	(4, 'Alexander', 'Robotnik', Null,'ar@robot.ru', '05/06/50', '1804899', 4, 4, 3, 3, 1),
	(5, 'Vladimir', 'Putin', '3712348','supervlad@red.ru', '16/07/63', '1805000', 5, 4, 3, 1, 2),
	(6, 'Paulo', 'Vicio', Null,'paolo@gmail.com', '22/08/85', '179245', 6, 5, 4, 2, 1);

INSERT INTO tipo_habitacion (id_tipo, precio, descripcion) VALUES
	(1, 605, 'Individual Estandar'),
	(2, 892, 'Doble Estandar'),
	(3, 1044, 'Doble Superior'),
	(4, 1500, 'Superior Family Plan'),
	(5, 1800, 'Suite Doble');

INSERT INTO habitacion (nro_habitacion, descuento, cantidad_de_dias, id_tipo) VALUES
	(1, 10, 5, 1),
	(2, 10, 5, 1),
	(3, 15, 7, 3),
	(4, 10, 5, 1),
	(5, 10, 5, 1),
	(6, 10, 6, 1),
	(7, 11, 7, 1),
	(8, 15, 15, 3),
	(9, 15, 15, 3),
	(10, 11, 6, 3),
	(11, 12, 7, 2),
	(12, 12, 7, 2),
	(13, 12, 7, 2),
	(14, 12, 7, 2),
	(15, 5, 5, 3),
	(16, 7, 7, 3),
	(17, 5, 5, 3),
	(18, 10, 7, 1),
	(19, 10, 7, 1),
	(20, 5, 5, 1),
	(21, 10, 5, 3),
	(22, 10, 7, 2),
	(23, 15, 10, 2),
	(24, 10, 7, 2),
	(25, 15, 15, 2),
	(26, 15, 15, 2),
	(27, 10, 10, 4),
	(28, 10, 10, 4),
	(29, 10, 10, 4),
	(30, 11, 11, 4),
	(31, 7, 5, 4),
	(32, 7, 5, 4),
	(33, 7, 5, 4),
	(34, 10, 7, 4),
	(35, 5, 20, 5),
	(36, 5, 20, 5),
	(37, 5, 7, 1),
	(38, 7, 10, 1),
	(39, 10, 12, 2),
	(40, 10, 12, 2),
	(41, 7, 10, 2),
	(42, 7, 10, 2),
	(43, 7, 10, 2),
	(44, 5, 7, 2),
	(45, 10, 15, 4),
	(46, 5, 7, 2),
	(47, 7, 10, 2),
	(48, 8, 11, 2),
	(50, 10, 15, 4);

INSERT INTO estadia (id_estadia, fecha_inicio, fecha_fin, nro_habitacion) VALUES
	(1, '10/12/2014', '15/12/2014', 1),
	(2, '01/01/2015', '05/01/2015', 7),
	(3, '01/01/2015', '05/01/2015', 6),
	(4, '03/02/2015', '13/02/2015', 19),
	(5, '05/03/2015', '25/03/2015', 17);


INSERT INTO mantenimiento (id_mantenimiento, fecha_inicio, fecha_fin, nro_habitacion) VALUES
	(1, '05/01/2015', '12/01/2015', 36),
	(2, '11/02/2015', '16/02/2015', 37),
	(3, '16/01/2015', '20/01/2015', 50),
	(4, '20/01/2015', '22/01/2015', 48),
	(5, '23/01/2015', '25/01/2015', 38),
	(6, '23/01/2015', '25/01/2015', 40),
	(7, '24/01/2015', '25/01/2015', 15),
	(8, '23/01/2015', '25/01/2015', 22),
	(9, '19/02/2015', '23/02/2015', 20),
	(10, '20/02/2015', '21/02/2015', 3);
	
	
INSERT INTO reserva (id_reserva, nombre, apellido, telefono, fecha_inicio, fecha_fin, nro_habitacion) VALUES
	(1, 'Alan', 'Moore', '150329076', '20/12/2014', '25/12/2014', 19),
	(2, 'Jorge Luis ', 'Borges', '1234567', '25/12/2014', '01/01/2015', 35);

INSERT INTO tiene_ocupante (id_pasajero, id_estadia) VALUES
	(3, 1),
	(1, 2),
	(2, 3),
	(6, 4),
	(4, 5),
	(5, 5);
