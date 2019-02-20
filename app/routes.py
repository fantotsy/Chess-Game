from flask import render_template, redirect, request
from app.dto.user import User
from app import app

USERNAME: str = "username"
PASSWORD: str = "password"

users = [User('user1', 'password1'), User('user2', 'password2'), User('user3', 'password3')]


@app.route('/', methods=['GET'])
@app.route('/login', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    username: str = request.form[USERNAME]
    password: str = request.form[PASSWORD]

    is_existing_user: bool = False
    for user in users:
        if user.username == username and user.password == password:
            is_existing_user = True
            break

    if is_existing_user:
        return redirect('/profile')
    else:
        return render_template('index.html', login_warning='Wrong credentials!')


@app.route('/signup', methods=['POST'])
def signup():
    username: str = request.form[USERNAME]
    password: str = request.form[PASSWORD]

    is_existing_user: bool = False
    for user in users:
        if user.username == username and user.password == password:
            is_existing_user = True
            break

    if is_existing_user:
        return render_template('index.html', signup_warning='Such username exists!')
    else:
        users.append(User(username, password))
        return redirect('/profile')


@app.route('/profile', methods=['GET'])
def profile():
    return render_template('profile.html')


@app.route('/game', methods=['POST'])
def game():
    return render_template('chessboard.html')
