import email
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


