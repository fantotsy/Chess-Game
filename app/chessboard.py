import string

from app.pieces import Color, Empty, Pawn, Rook, Knight, Bishop, Queen, King
from app.position import Position
from app.repository import Repository

POSITIONS_DELIMITER = ':'
MOVEMENTS_DELIMITER = '#'

repository = Repository()


class Chessboard(object):

    def __init__(self):
        self.movements_history = []
        self.current_player_color = Color.WHITE
        self.captured_white_pieces = []
        self.captured_black_pieces = []
        self.board = [
            [Rook(Color.WHITE), Pawn(Color.WHITE), Empty(), Empty(), Empty(), Empty(), Pawn(Color.BLACK), Rook(Color.BLACK)],
            [Knight(Color.WHITE), Pawn(Color.WHITE), Empty(), Empty(), Empty(), Empty(), Pawn(Color.BLACK), Knight(Color.BLACK)],
            [Bishop(Color.WHITE), Pawn(Color.WHITE), Bishop(Color.BLACK), Empty(), Empty(), Empty(), Pawn(Color.BLACK), Bishop(Color.BLACK)],
            [Queen(Color.WHITE), Pawn(Color.WHITE), Empty(), Bishop(Color.WHITE), Empty(), Empty(), Pawn(Color.BLACK), Queen(Color.BLACK)],
            [King(Color.WHITE), Pawn(Color.WHITE), Empty(), Empty(), Bishop(Color.BLACK), Empty(), Pawn(Color.BLACK), King(Color.BLACK)],
            [Bishop(Color.WHITE), Pawn(Color.WHITE), Empty(), Empty(), Empty(), Empty(), Pawn(Color.BLACK), Bishop(Color.BLACK)],
            [Knight(Color.WHITE), Pawn(Color.WHITE), Empty(), Empty(), Empty(), Empty(), Pawn(Color.BLACK), Knight(Color.BLACK)],
            [Rook(Color.WHITE), Pawn(Color.WHITE), Empty(), Empty(), Empty(), Empty(), Pawn(Color.BLACK), Rook(Color.BLACK)]
        ]

    def is_piece_allowed(self, position):
        current_position = self.parse_position(position)
        piece = self.board[current_position.x][current_position.y]
        return piece.color == self.current_player_color

    def get_targets_of_unparsed_position(self, position):
        current_position = self.parse_position(position)
        return self.get_targets_of_parsed_position(current_position)

    def get_targets_of_parsed_position(self, position: Position):
        piece = self.board[position.x][position.y]
        targets = piece.get_targets(position, self.board)

        result = []
        for target in targets:
            if not self.is_self_check_possible(position, target):
                result.append(string.ascii_lowercase[target.x] + str(target.y + 1))
        return result

    def perform_movement(self, position, target):
        current_position = self.parse_position(position)
        target_position = self.parse_position(target)

        target_piece = self.board[target_position.x][target_position.y]
        if target_piece.color == Color.WHITE:
            self.captured_white_pieces.append(target_piece)
        else:
            self.captured_black_pieces.append(target_piece)
        self.board[target_position.x][target_position.y] = self.board[current_position.x][current_position.y]
        self.board[current_position.x][current_position.y] = Empty()
        self.current_player_color *= (-1)
        self.movements_history.append(self.construct_movement_string(current_position, target_position))

        return self.is_check_for_current_player()

    def parse_position(self, position):
        x_position = string.ascii_lowercase.index(position[0])  # x position is from left to right
        y_position = int(position[1]) - 1  # y position is from down to up
        return Position(x_position, y_position)

    def get_king_position(self, color):
        for x_index, line in enumerate(self.board):
            for y_index, square in enumerate(line):
                if square == King(color):
                    return Position(x_index, y_index)

    def is_self_check_possible(self, position, target):
        target_piece = self.board[target.x][target.y]
        self.board[target.x][target.y] = self.board[position.x][position.y]
        self.board[position.x][position.y] = Empty()

        result = self.is_check_for_current_player()

        self.board[position.x][position.y] = self.board[target.x][target.y]
        self.board[target.x][target.y] = target_piece

        return result

    def is_check_for_current_player(self):
        king_position = self.get_king_position(self.current_player_color)

        for x_index, line in enumerate(self.board):
            for y_index, square in enumerate(line):
                if square.color == self.current_player_color * (-1):
                    for target in square.get_targets(Position(x_index, y_index), self.board):
                        if king_position == target:
                            return True
        return False

    def is_checkmate_for_current_player(self):
        if not self.is_check_for_current_player():
            return False
        else:
            for x_index, line in enumerate(self.board):
                for y_index, square in enumerate(line):
                    if square.color == self.current_player_color:
                        targets = self.get_targets_of_parsed_position(Position(x_index, y_index))
                        if len(targets) > 0:
                            return False
        return True

    def save_game(self):
        repository.save_game('Test Game', MOVEMENTS_DELIMITER.join(self.movements_history))

    def construct_movement_string(self, current_position, target_position):
        parsed_current_position = string.ascii_lowercase[current_position.x] + str(current_position.y + 1)
        parsed_target_position = string.ascii_lowercase[target_position.x] + str(target_position.y + 1)
        return POSITIONS_DELIMITER.join([parsed_current_position, parsed_target_position])

    def get_games(self):
        return repository.get_games()

    def get_game_activity(self, game_name):
        result = []
        game_activity = repository.get_game(game_name)[0]
        movements = game_activity.split(MOVEMENTS_DELIMITER)
        for movement in movements:
            result.append(movement.split(POSITIONS_DELIMITER))
        return result
