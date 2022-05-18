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

CREATE PROCEDURE ObtenerUsuarioConContraseña(
  IN insertUsuario VARCHAR(40), IN insertPassword VARCHAR(40))
  BEGIN
  SELECT * FROM Usuarios
  WHERE nickname = insertUsuario AND password = insertPassword;
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
