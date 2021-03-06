SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
FROM ((Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID);

SELECT Clases.id, Clases.codigoAula, Alumnos.nombre, Materias.nombre, 
Grupos.nombre, Profesor.nombre
FRON

SELECT UsuarioProfesor.id, Profesores.nombre, Usuarios.nickname, Usuarios.password 
FROM ((UsuarioProfesor
INNER JOIN Profesores ON UsuarioProfesor.id = Profesores.id)
INNER JOIN Usuarios ON UsuarioProfesor.id = Usuarios.id)

CREATE VIEW vw_clases AS
SELECT Alumnos.nombre AS ALUMNO, Materias.nombre AS MATERIA, Grupos.letraGrupo AS GRUPO, 
Grupos.gradoGrupo AS GRADO, Profesores.nombre AS PROFESOR, Clases.cicloEscolar AS CICLOESCOLAR
FROM ((((Clases
INNER JOIN Alumnos ON Clases.idAlumno = Alumnos.id)
INNER JOIN Materias ON Clases.idMateria = Materias.id)
INNER JOIN Grupos ON Clases.idGrupo = Grupos.id)
INNER JOIN Profesores ON Clases.idProfesor = Profesores.id);

SELECT Clases.id, Alumnos.nombre, Materias.nombre, Grupos.nombre, Profesores.nombre, Clases.cicloEscolar
FROM Clases
INNER JOIN Alumnos ON Clases.idAlumnos = Alumnos.id;

CREATE PROCEDURE ObtenerUsuarioConContrase├▒a(
  IN insertUsuario VARCHAR(40), IN insertPassword VARCHAR(40))
  BEGIN
  SELECT * FROM Usuarios
  WHERE nickname = insertUsuario AND password = insertPassword;
  END

CREATE PROCEDURE ObtenerUsuarioProfesorConContrase├▒a( /*REVISAR TEMA DE USUARIOS*/
    IN insertUsuario VARCHAR(40), IN insertPassword VARCHAR(40))
    BEGIN
    SELECT UsuarioProfesor.id, Profesores.nombre, Usuarios.nickname, Usuarios.password 
    FROM ((UsuarioProfesor
    INNER JOIN Profesores ON UsuarioProfesor.id = Profesores.id)
    INNER JOIN Usuarios ON UsuarioProfesor.id = Usuarios.id) 
    WHERE Usuarios.nickname = insertUsuario AND Usuarios.password = insertPassword;
    END

CREATE TABLE UsuarioProfesor(
    id INT NOT NULL AUTO_INCREMENT,
    idProfesor INT NOT NULL,
    idUsuario INT NOT NULL,
    PRIMARY  KEY(id),
    FOREIGN KEY(idProfesor) REFERENCES Profesores(id),
    FOREIGN KEY(idUsuario) REFERENCES Usuarios(id)
);

CREATE TABLE UsuarioProfesor(
    id INT NOT NULL AUTO_INCREMENT,
    idProfesor INT NOT NULL,
    idUsuario INT NOT NULL,
    PRIMARY  KEY(id),
    FOREIGN KEY(idProfesor) REFERENCES Profesores(id),
    FOREIGN KEY(idUsuario) REFERENCES Usuarios(id)
);

CREATE TABLE UsuarioAlumno(
    id INT NOT NULL AUTO_INCREMENT,
    idAlumno INT NOT NULL,
    idUsuario INT NOT NULL,
    PRIMARY  KEY(id),
    FOREIGN KEY(idAlumno) REFERENCES Alumnos(id),
    FOREIGN KEY(idUsuario) REFERENCES Usuarios(id)
);

INSERT INTO Usuarios(nickname, password, levelAdministration) VALUES('fran89',  '1234', 2);

CREATE PROCEDURE ObtenerUsuarioProfesorConContrase├▒a(
    IN insertUsuario VARCHAR(40), IN insertPassword VARCHAR(40))
    BEGIN
    SELECT UsuarioProfesor.id, Profesores.nombre, Usuarios.nickname, Usuarios.password 
    FROM ((UsuarioProfesor
    INNER JOIN Profesores ON UsuarioProfesor.id = Profesores.id)
    INNER JOIN Usuarios ON UsuarioProfesor.id = Usuarios.id) 
    WHERE Usuarios.nickname = insertUsuario AND Usuarios.password = insertPassword;
    END

CREATE PROCEDURE RegistrarAlumno(
IN insertNombre VARCHAR(100), insertEmail VARCHAR(100), insertFechaNaci DATE, insertGenero VARCHAR(40))
BEGIN
  INSERT INTO Alumnos (nombre, email, fechaNaci, genero, vigencia) 
  VALUES (insertNombre, insertEmail, insertFechaNaci, insertGenero, 'True');
END

CREATE PROCEDURE ObtenerUsuarioConContrase├▒a(
  IN insertUsuario VARCHAR(40), IN insertPassword VARCHAR(40))
  BEGIN
  SELECT * FROM Usuarios
  WHERE nickname = insertUsuario AND password = insertPassword;
  END
  
 CREATE PROCEDURE ObtenerUsuarioProfesorConContrase├▒a(
  IN insertUsuario VARCHAR(40), IN insertPassword VARCHAR(40))
  BEGIN
  SELECT * FROM Usuarios
  WHERE nickname = insertUsuario AND password = insertPassword;
  END

CREATE PROCEDURE darBajaAlumno(
IN idAlumno INT)
BEGIN
UPDATE Alumnos SET vigencia = 'False'
WHERE id = idAlumno;
END

CREATE PROCEDURE darAltaAlumno(
  IN idAlumno INT)
  BEGIN 
  UPDATE Alumnos SET vigencia = 'True'
  WHERE id = idAlumno;
  END

CREATE PROCEDURE darBajaProfesor(
  IN idProfesor INT)
  BEGIN 
  UPDATE Profesores SET vigencia = 'False'
  WHERE id = idProfesor;
  END

CREATE PROCEDURE darAltaProfesor(
  IN idProfesor INT)
  BEGIN 
  UPDATE Profesores SET vigencia = 'True'
  WHERE id = idProfesor;
  END

CREAR PROCEDURE CAMBIAR PROFESOR
LO MISMO CON PROFESORES

CREATE PROCEDURE registroClaseAlumno(
  IN insertCodigoAula VARCHAR(4), insertIdAlumno INT, insertIdMateria INT, insertIdGrupo int, insertIdProfesor INT)
  BEGIN
  INSERT INTO Clases 
  (codigoAula, idAlumno, idMateria, idGrupo, idProfesor, cicloEscolar) 
  VALUES (insertCodigoAula, insertIdAlumno, insertIdMateria, insertIdGrupo, insertIdProfesor, '2021-A');
  END
