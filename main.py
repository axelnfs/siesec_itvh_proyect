#flask
from flask import Flask, make_response, render_template, make_response, session, redirect, request, flash, url_for
from flask_wtf import FlaskForm
#bootstrap
from flask_bootstrap import Bootstrap
#paquetes locales
from app.forms import LoginForm
from app.forms import RegisterForm
from app.forms import CreateTheacherForm
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

def getUser(nickname, password):
    conexion = obtener_conexion()
    user = []
    with conexion.cursor() as cursor:
        sql = "SELECT * FROM Usuarios WHERE nickname = %s;"
        cursor.execute(sql, nickname)
        for x in cursor:
            user = x
        # user = cursor.fetchall()
    conexion.close()
    if not user:
        return '''<h1>error</h1>'''
    else:
        if nickname == user[1] and password == user[2]:
            session['nickname'] = user[1]
            return redirect(url_for('index'))
        else:
            return redirect(url_for('register'))

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
    
@app.route('/login', methods=["GET", "POST"])
def login():
    session.clear()
    login_form = LoginForm()
    nickname = session.get('nickname')
    session['nickname'] = nickname
    context = {
        'login_form': login_form,
    }
    if login_form.validate_on_submit:
        nickname = login_form.nickname.data
        password = login_form.password.data
        if 'submit' in request.form:
            getUser(nickname, password)
    return render_template('login.html', **context)

@app.route('/teachers')
def teachers():
    connection = obtener_conexion()
    teachers = []
    linkCreateTeachers = False
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Profesores")
        teachers = cursor.fetchall()
    connection.close()
    context = {
        'linkCreateTeachers': linkCreateTeachers,
    }
    if session.get('nickname') == 'kylo':
        linkCreateTeachers = True
        return render_template('teachers.html',  teachers = teachers, **context)
    else:
        return render_template('teachers.html',  teachers = teachers, **context)

@app.route('/teachers/create')
def createTeachers():
    createTeacher_form = CreateTheacherForm()
    nickname = session.get('nickname')
    context = {
        'createTeacher_form': createTeacher_form,
    }
    if session.get('nickname') == 'kylo':
        if createTeacher_form.validate_on_submit:
            nombre = createTeacher_form.nombre.data
            fechaNaci = createTeacher_form.fechaNaci.data
            genero = createTeacher_form.genero.data
        return render_template('teachersform.html', **context)
    else:
        return redirect('/index')

@app.route('/logout')
def logout():
    session.clear()
    return render_template('index.html')