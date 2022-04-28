from flask import Flask, make_response, render_template, make_response, session, redirect, request, flash
from flask_wtf import FlaskForm
from app.forms import LoginForm
from app.forms import RegisterForm

app = Flask(__name__, template_folder='app/templates')
app.secret_key = "1234"
# formLogin = LoginForm(request.form)

@app.before_request
def session_managment():
    session.permanent = True

@app.route('/')
def hello():
    response = make_response(redirect('/index'))
    return response

@app.route('/register')
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        nickname = register_form.nickname.data
        password = register_form.password.data
        levelAdministration = register_form.levelAdministration.data
        flash('Registro exitoso')

    return render_template('register.html', form = register_form)
    
@app.route('/login')
def login():
    session.clear()
    login_form = LoginForm()
    # session['user'] = 'pepe'
    # session["auth"] = 1

    # context = {
    #     'login_form': login_form
    # }

    return render_template('login.html', form = login_form)

@app.route('/')
def index():
    try:
        user = session["user"]
        auth = session["auth"]
    except:
        user = "unknown"
        auth = 0
    
@app.route('/logout')
def logout():
    session.clear()
    session["user"] = "unknown"
    session["auth"] = 0
    return index()