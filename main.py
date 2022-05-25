#flask
from flask import Flask, make_response, render_template, make_response, session, redirect, request, flash, url_for
from flask_wtf import FlaskForm
#bootstrap
from flask_bootstrap import Bootstrap
#paquetes locales
from app.forms import CreateStudentForm, LoginForm, UpStudentForm
from app.forms import RegisterForm
from app.forms import CreateTheacherForm
from app.forms import CreateStudentForm
from app.forms import DownStudentForm
from app.forms import UpStudentForm
from app.forms import DownTeacherForm
from app.forms import UpTeacherForm
# from app.forms import SearchTeacherForm
#mysql
from bd import obtener_conexion 
#python
from system import generateRecovery

app = Flask(__name__, 
template_folder='app/templates', 
static_folder='app/static')

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

def downStudent(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = "CALL darBajaAlumno("+id+");"
        cursor.execute(sql)
    conexion.commit()
    conexion.close()

def upStudent(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = "CALL darAltaAlumno(%s);"
        cursor.execute(sql, (id))
    conexion.commit()
    conexion.close()

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
def loginTeacher():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    if login_form.validate_on_submit:
        nickname = login_form.nickname.data
        password = login_form.password.data
        user = []
        if 'submit' in request.form:
            conexion = obtener_conexion() #REVISAR USUARIOS PROCEDURE PROFESORES
            with conexion.cursor() as cursor:
                sql = "CALL ObtenerUsuarioProfesorConContraseña('"+nickname+"', '"+password+"');"
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
    if session.get('nickname') == 'kylo' & 'admin':
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
            cursor.execute("SELECT * FROM vw_clases;")
            classrooms = cursor.fetchall()
        connection.close()
        return render_template('classrooms.html', classrooms = classrooms)
    else:
        return redirect('/index')

@app.route('/students/new', methods=["GET", "POST"]) 
def newStudentClassroom():
    if session.get('nickname'):
        createStudent_form = CreateStudentForm()
        context = {
            'createStudent_form': createStudent_form
        }
        if createStudent_form.validate_on_submit:
            nombre = createStudent_form.nombre.data
            email = createStudent_form.email.data
            fechaNaci = createStudent_form.fechaNaci.data
            genero = createStudent_form.genero.data
            if 'submit' in request.form:
                connection = obtener_conexion()
                with connection.cursor() as cursor:
                    sql = "CALL RegistrarAlumno('"+nombre+"', '"+email+"','"+fechaNaci+"', '"+genero+"');"
                    cursor.execute(sql)
                connection.commit()
                connection.close()
                return redirect('/students')
        return render_template('createStudent.html', **context)
    else:
        return redirect('/index')
    
@app.route('/students')
def students():
    if session.get('nickname'):
        connection = obtener_conexion()
        students = []
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Alumnos;")
            students = cursor.fetchall()
        connection.close()
        return render_template('students.html', students = students)
    else:
        return redirect('/index')

@app.route('/students/downstudent', methods=["GET", "POST"])
def downStudent():
    if session.get('nickname'):
        downStudent_form = DownStudentForm()
        context = {
            'downStudent_form': downStudent_form
        }
        if downStudent_form.validate_on_submit:
            id = downStudent_form.id.data
            if 'submit' in request.form:
                conexion = obtener_conexion()
                with conexion.cursor() as cursor:
                    sql = "CALL darBajaAlumno("+id+");"
                    cursor.execute(sql)
                conexion.commit()
                conexion.close()
                return redirect('/students')
        return render_template('downstudentform.html', **context)
    else:
        return redirect('/index')

@app.route('/students/upstudent', methods=["GET", "POST"])
def upStudent():
    if session.get('nickname'):
        upStudent_form = UpStudentForm()
        context = {
            'upStudent_form':upStudent_form
        }
        if upStudent_form.validate_on_submit:
            id = upStudent_form.id.data
            if 'submit' in request.form:
                conexion = obtener_conexion()
                with conexion.cursor() as cursor:
                    sql = "CALL darAltaAlumno("+id+");"
                    cursor.execute(sql)
                conexion.commit()
                conexion.close()
                return redirect('/students')
        return render_template('upstudentform.html', **context)
    else:
        return redirect('/index')
        
@app.route('/teachers/upteacher', methods=["GET", "POST"])
def upTeacher():
    if session.get('nickname'):
        upTeacher_form = UpTeacherForm()
        context = {
            'upTeacher_form':upTeacher_form
        }
        if upTeacher_form.validate_on_submit:
            id = upTeacher_form.id.data
            if 'submit' in request.form:
                conexion = obtener_conexion()
                with conexion.cursor() as cursor:
                    sql = "CALL darAltaProfesor("+id+");"
                    cursor.execute(sql)
                conexion.commit()
                conexion.close()
                return redirect('/teachers')
        return render_template('upteachersform.html', **context)
    else:
        return redirect('/index')

@app.route('/teachers/downteacher', methods=["GET", "POST"])
def downTeacher():
    if session.get('nickname'):
        downTeacher_form = DownTeacherForm()
        context = {
            'downTeacher_form':downTeacher_form
        }
        if downTeacher_form.validate_on_submit:
            id = downTeacher_form.id.data
            if 'submit' in request.form:
                conexion = obtener_conexion()
                with conexion.cursor() as cursor:
                    sql = "CALL darBajaProfesor("+id+");"
                    cursor.execute(sql)
                conexion.commit()
                conexion.close()
                return redirect('/teachers')
        return render_template('downteacherform.html', **context)
    else:
        return redirect('/index')

@app.route('/logout')
def logout():
    session.clear()
    generateRecovery()
    return render_template('index.html')