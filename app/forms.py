from flask_wtf import FlaskForm
from wtforms import Form
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators={DataRequired()})
    password = PasswordField('Password', validators={DataRequired()})
    submit = SubmitField('Enviar')

class RegisterForm(FlaskForm):
    nickname = StringField('Nombre de usuario', validators=[DataRequired()])
    password = StringField('Contrasena', validators=[DataRequired()])
    levelAdministration = StringField('Nivel de administracion', validators=[DataRequired()])
    submit = SubmitField('Enviar')


