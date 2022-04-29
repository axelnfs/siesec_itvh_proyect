#flask
from click import password_option
from flask import Flask, make_response, render_template, make_response, session, redirect, request, flash, url_for
from flask_wtf import FlaskForm
#bootstrap
from flask_bootstrap import Bootstrap
#paquetes locales
from app.forms import LoginForm
from app.forms import RegisterForm
#mysql
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "admin"
    password = "Lexa1990."
    database = 
)

app = Flask(__name__, template_folder='app/templates')
bootstrap = Bootstrap(app)
app.secret_key = "1234"

@app.route('/') 
def hello(): #revisar
    response = make_response(redirect('/index'))
    return response

@app.route('/index')
def index():
    nickname = session.get('nickname')
    if nickname == None:
        return render_template('failure.html')
    else:
        return render_template('index.html', nickname = nickname)

@app.route('/register', methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    nickname = session.get('nickname')

    context = {
        'register_form': register_form,
        'username': nickname
    }

    if register_form.validate_on_submit:
        nickname = register_form.nickname.data
        password = register_form.password.data
        levelAdministration = register_form.levelAdministration.data
        session['nickname'] = nickname
    return render_template('register.html', **context)
    
@app.route('/login')
def login():
    session.clear()
    login_form = LoginForm()

    return render_template('login.html', form = login_form)

# @app.route('/')
# def index():
#     try:
#         user = session["user"]
#         auth = session["auth"]
#     except:
#         user = "unknown"
#         auth = 0
    
@app.route('/logout')
def logout():
    session.clear()
    return render_template('index.html')