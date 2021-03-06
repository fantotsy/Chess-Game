from flask import render_template, request, jsonify

from app import app
from app.chessboard import Chessboard

chessboard = Chessboard()


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    games = chessboard.get_games()
    return render_template('index.html', games=games)


@app.route('/game', methods=['GET'])
def game():
    return render_template('chessboard.html', board=chessboard.board)


@app.route('/targets', methods=['POST'])
def targets():
    current_position = request.form['position']
    if chessboard.is_piece_allowed(current_position):
        target_positions = chessboard.get_targets_of_unparsed_position(current_position)
        return jsonify(targets=target_positions)
    else:
        return jsonify('Piece is forbidden for current player'), 400


@app.route('/movement', methods=['POST'])
def movement():
    current_position = request.form['position']
    target_position = request.form['target']

    is_check_for_next_player = chessboard.perform_movement(current_position, target_position)
    if is_check_for_next_player:
        is_checkmate_for_next_player = chessboard.is_checkmate_for_current_player()
        return jsonify(isCheck=is_check_for_next_player, isCheckmate=is_checkmate_for_next_player)
    else:
        return jsonify(isCheck=is_check_for_next_player, isCheckmate=False)


@app.route('/save', methods=['POST'])
def save():
    chessboard.save_game()
    return jsonify(success=True)


@app.route('/replay', methods=['GET'])
def replay():
    game_name = request.args.get('game')
    game_activity = chessboard.get_game_activity(game_name)
    return jsonify(activity=game_activity)
