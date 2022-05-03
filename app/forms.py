from flask_wtf import FlaskForm
from wtforms import Form
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    nickname = StringField('Nombre de usuario', validators={DataRequired()})
    password = PasswordField('Password', validators={DataRequired()})
    submit = SubmitField('Enviar')

class RegisterForm(FlaskForm):
    nickname = StringField('Nombre de usuario', validators=[DataRequired()])
    password = StringField('Contrasena', validators=[DataRequired()])
    levelAdministration = StringField('Nivel de administracion', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class CreateTheacherForm(FlaskForm):
    nombre = StringField('Nombre de usuario', validators=[DataRequired()])
    fechaNaci = StringField('Fecha Nacimiento', validators=[DataRequired()])
    genero = StringField('Genero', validators=[DataRequired()])
    Submit = SubmitField('Enviar')

