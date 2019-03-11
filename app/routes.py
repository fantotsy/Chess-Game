from flask import render_template, request, jsonify, abort

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


@app.route('/targets', methods=['POST'])
def targets():
    current_position = request.form['position']
    if chessboard.is_piece_allowed(current_position):
        target_positions = chessboard.get_targets(current_position)
        return jsonify(targets=target_positions)
    else:
        return jsonify('Piece is forbidden for current player'), 400


@app.route('/movement', methods=['POST'])
def movement():
    current_position = request.form['position']
    target_position = request.form['target']
    is_check = chessboard.perform_movement(current_position, target_position)
    return jsonify(isCheck=is_check)
