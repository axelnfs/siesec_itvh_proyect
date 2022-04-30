#flask
from distutils.util import execute
from click import password_option
from flask import Flask, make_response, render_template, make_response, session, redirect, request, flash, url_for
from flask_wtf import FlaskForm
#bootstrap
from flask_bootstrap import Bootstrap
#paquetes locales
from app.forms import LoginForm
from app.forms import RegisterForm
#mysql
from bd import obtener_conexion

app = Flask(__name__, template_folder='app/templates')
bootstrap = Bootstrap(app)
app.secret_key = "1234"

def createUser(nickname, password, levelAdministration):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = "INSERT INTO Usuarios(nickname, password, levelAdministration) VALUES (%s,%s,%s)"
        cursor.execute(sql, (nickname, password, levelAdministration))
    conexion.commit()
    conexion.close()
    session['nickname'] = nickname
    return redirect(url_for('index'))
    

@app.route('/') 
def hello(): #revisar
    response = make_response(redirect('/index'))
    return response

@app.route('/index')
def index():
    nickname = session.get('nickname')
    return render_template('index.html', nickname = nickname)

@app.route('/register', methods=["GET", "POST"])
def register():
    if session.get('nickname') == True:
        return redirect('index.html')

    register_form = RegisterForm()
    nickname = session.get('nickname')
    session['nickname'] = nickname
    context = {
        'register_form': register_form,
    }

    if register_form.validate_on_submit:
        nickname = register_form.nickname.data
        password = register_form.password.data
        levelAdministration = register_form.levelAdministration.data
        if 'submit' in request.form:
            createUser(nickname, password, levelAdministration)
    return render_template('register.html', **context)
    
@app.route('/login')
def login():
    session.clear()
    login_form = LoginForm()
    return render_template('login.html', form = login_form)

@app.route('/teachers')
def teachers():
    connection = obtener_conexion()
    teachers = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Profesores")
        teachers = cursor.fetchall()
    connection.close()
    return render_template('teachers.html',  teachers = teachers)

    
@app.route('/logout')
def logout():
    session.clear()
    return render_template('index.html')