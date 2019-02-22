from flask import render_template

from app import app
from app.chessboard import Chessboard

chessboard = Chessboard()


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/game', methods=['GET'])
def game():
    return render_template('chessboard.html', board=chessboard.board)
