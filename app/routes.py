from flask import render_template

from app import app
from app.chessboard import Chessboard


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/game', methods=['GET'])
def game():
    print(Chessboard())
    return render_template('chessboard.html')
