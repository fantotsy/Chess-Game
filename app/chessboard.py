import string

from app.pieces import Color, Empty, Pawn, Rook, Knight, Bishop, Queen, King
from app.position import Position


class Chessboard(object):

    def __init__(self):
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

    def get_targets(self, position):
        current_position = self.parse_position(position)
        piece = self.board[current_position.x][current_position.y]
        targets = piece.get_targets(current_position, self.board)

        result = []
        for target in targets:
            if not self.is_self_check_possible(current_position, target):
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

        return

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

        result = self.is_check_for_player(self.current_player_color)

        self.board[position.x][position.y] = self.board[target.x][target.y]
        self.board[target.x][target.y] = target_piece

        return result

    def is_check_for_player(self, player_color):
        king_position = self.get_king_position(player_color)

        for x_index, line in enumerate(self.board):
            for y_index, square in enumerate(line):
                if square.color == player_color * (-1):
                    for target in square.get_targets(Position(x_index, y_index), self.board):
                        if king_position == target:
                            return True
        return False
