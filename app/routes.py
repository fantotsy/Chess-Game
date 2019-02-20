from flask import render_template, redirect, request
from app import app

USERNAME = "username"
PASSWORD = "password"


@app.route('/', methods=['GET'])
@app.route('/login', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form[USERNAME]
    password = request.form[PASSWORD]

    if username == password:
        return redirect('/profile')
    else:
        return render_template('index.html', login_warning='Wrong credentials!')


@app.route('/signup', methods=['POST'])
def signup():
    username = request.form[USERNAME]
    password = request.form[PASSWORD]

    if username == password:
        return redirect('/profile')
    else:
        return render_template('index.html', signup_warning='Such username exists!')


@app.route('/profile', methods=['GET'])
def profile():
    return render_template('profile.html')
