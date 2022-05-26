import email
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import Form
from wtforms.fields import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    nickname = StringField('',validators={DataRequired()}, render_kw={"placeholder": "Nombre de Usuario"})
    password = PasswordField('', validators={DataRequired()}, render_kw={"placeholder": "Contraseña"})
    submit = SubmitField('Entrar')

class RegisterForm(FlaskForm):
    nickname = StringField('Nombre de usuario', validators=[DataRequired()])
    password = StringField('Contrasena', validators=[DataRequired()])
    levelAdministration = StringField('Nivel de administracion', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class CreateTheacherForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    fechaNaci = StringField('Fecha Nacimiento', validators=[DataRequired()])
    genero = StringField('Genero', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class SearchTeacherForm(FlaskForm):
    id = StringField('ID')
    submit = SubmitField('Buscar')

class CreateStudentForm(FlaskForm):
    nombre = StringField('nombre')
    email = StringField('Email')
    fechaNaci = StringField('Fecha Nacimiento')
    genero = StringField('Genero')
    submit = SubmitField('REGISTRAR')

class DownStudentForm(FlaskForm):
    id = StringField('ID')
    submit = SubmitField('DAR BAJA')

class UpStudentForm(FlaskForm):
    id = StringField('ID')
    submit = SubmitField('DAR ALTA')

class DownTeacherForm(FlaskForm):
    id = StringField('ID')
    submit = SubmitField('DAR BAJA')

class UpTeacherForm(FlaskForm):
    id = StringField('ID')
    submit = SubmitField('DAR ALTA')
    
class registerStudentClass(FlaskForm):
    codigoAula = StringField('Aula')
    idAlumno = StringField('id Alumno')
    idMateria = SelectField('Programming Language', choices=[('1', 'HISTORIA 1'), ('2', 'MATEMATICAS 1'), ('3', 'LITERATURA 1'), ('4','CIENCIAS 1'), ('5', 'FISICA 1')])
    idGrupo = SelectField('Grupo', choices=[('1','A')])
    idProfesor = StringField('id Profesor')

