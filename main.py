#flask
from re import A
from sqlite3 import connect
from flask import Flask, make_response, render_template, make_response, session, redirect, request, flash, url_for
from flask_wtf import FlaskForm
#bootstrap
from flask_bootstrap import Bootstrap
#paquetes locales
from app.forms import LoginForm
from app.forms import RegisterForm
from app.forms import CreateTheacherForm
# from app.forms import SearchTeacherForm
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

def createTeacher(nombre, fechaNaci, genero, vigencia):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = "INSERT INTO Profesores(nombre, fechaNaci, genero, vigencia) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nombre, fechaNaci, genero, vigencia))
    conexion.commit()
    conexion.close()
    redirect(url_for('teachers'))

@app.route('/') 
def hello(): #revisar
    response = make_response(redirect('/index'))
    return response

@app.route('/index')
def index():
    nickname = session.get('nickname')
    showMoreMenu = False

    if session.get('nickname') == True:
        showMoreMenu = True
        return render_template('index.html', nickname = nickname, showMoreMenu = showMoreMenu)
    else:
        return render_template('index.html', nickname = nickname, showMoreMenu = showMoreMenu)

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

@app.route('/login', methods=["GET","POST"])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    if login_form.validate_on_submit:
        nickname = login_form.nickname.data
        password = login_form.password.data
        user = []
        if 'submit' in request.form:
            conexion = obtener_conexion()
            with conexion.cursor() as cursor:
                sql = "CALL ObtenerUsuarioProfesorConContraseña('"+nickname+"', '"+password+"');"
                cursor.execute(sql)
                for x in cursor:
                    user = x[1]
            conexion.close()

@app.route('/login/admin', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form,
    }
    if login_form.validate_on_submit:
        nickname = login_form.nickname.data
        password = login_form.password.data
        user = []
        if 'submit' in request.form:
            conexion = obtener_conexion()
            with conexion.cursor() as cursor:
                sql = "CALL ObtenerUsuarioConContraseña('"+nickname+"', '"+password+"');"
                cursor.execute(sql)
                for x in cursor:
                    user = x[1]
            conexion.close()
            nickname = user
            if nickname == False:
                return render_template('errorUsuario.html')
            else:
                session['nickname'] = nickname
                nickname = session['nickname']
                return render_template('index.html', nickname = nickname)
    return render_template('login.html', **context)

@app.route('/teachers')
def teachers():
    connection = obtener_conexion() #lectura de todos 
    teachers = []
    nickname = session.get('nickname')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Profesores")
        teachers = cursor.fetchall()
    connection.close()
    return render_template('teachers.html',  teachers = teachers)

@app.route('/teachers/create', methods=["GET", "POST"])
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
            if 'submit' in request.form:
                createTeacher(nombre, fechaNaci, genero, vigencia='true')
                return render_template('teachers.html')
        return render_template('teachersform.html', **context)
    else:
        return redirect('/index')

@app.route('/classrooms')
def classrooms():
    if session.get('nickname'):
        connection = obtener_conexion()
        classrooms =  [] 
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Alumnos")
            classrooms = cursor.fetchall()
        connection.close()
        return render_template('classrooms.html', students = students)
    else:
        return redirect('/index')

# @app.route('/teachers/search', methods=["GET"])
# def searchTeacher():
#     searchTeacher_form = SearchTeacherForm()
#     context = {
#         'searchTeacher_form': searchTeacher_form
#     }
#     if 'submit' in request.form:
#         id = request.args.get('id')
#         searchTeacher(id)
#     return render_template('searchTeacher.html', **context)
# # NOTA: ANDABA USANDO DOS FUNCIONES, UNA RECIBE Y OTRA ENVIA
# # @app.route('/teachers/search/result')
# def searchIdTeacher(id):
#     teacher = []
#     context = {
#         'teacher': teacher
#     }
#     connection = obtener_conexion()
#     with connection.cursor() as cursor:
#         sql = "SELECT * FROM Profesores WHERE id = %s"
#         cursor.execute(sql, (id))
#         teacher = cursor.fetchall()
#     connection.close()
#     return redirect('teacherinfo.html', **context)
#     # searchTeacher_form = SearchTeacherForm()
#     # teacher = []
#     # context = {
#     #     'searchTeacher_form': searchTeacher_form,
#     #     'teacher': teacher
#     # }
#     # if searchTeacher_form.validate_on_submit:
#     #     id = searchTeacher_form.id.data
#     #     connection = obtener_conexion()
#     #     if 'sumbit' in request.form:
#     #         with connection.cursor() as cursor:
#     #             sql = "SELECT * FROM Profesores WHERE id = %s"
#     #             cursor.execute(sql, (id))
#     #             teacher = cursor.fetchall()
#     #         connection.close()
#     #         return render_template('searchTeacher.html', **context)
#     # return render_template('searchTeacher.html', **context)

@app.route('/students')
def students():
    if session.get('nickname') == 'kylo':
        connection = obtener_conexion()
        students = []
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Alumnos")
            students = cursor.fetchall()
        connection.close()
        return render_template('students.html', students = students)
    else:
        return redirect('/index')

@app.route('/logout')
def logout():
    session.clear()
    return render_template('index.html')