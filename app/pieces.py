class Color(object):
    EMPTY = 0
    WHITE = 1
    BLACK = 2


class Piece(object):
    image = None

    def __init__(self, color):
        self.color = color

    def __repr__(self):
        if self.color == Color.WHITE:
            return self.image[0]
        else:
            return self.image[1]


class Empty(object):
    color = Color.EMPTY

    def get_moves(self):
        raise Exception('Empty square does not have moves!')

    def __repr__(self):
        return ''


class Pawn(Piece):
    image = ('♙', '♟')

    def get_moves(self):
        if self.color == Color.WHITE:
            return [[-1, 1], [0, 1], [1, 1]]
        else:
            return [[-1, -1], [0, -1], [1, -1]]


class Rook(Piece):
    image = ('♖', '♜')

    def get_moves(self):
        return [
            [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0],  # right
            [-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0],  # left
            [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7],  # up
            [0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7]  # down
        ]


class Knight(Piece):
    image = ('♘', '♞')

    def get_moves(self):
        return [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]


class Bishop(Piece):
    image = ('♗', '♝')

    def get_moves(self):
        return [
            [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7],  # right-up
            [1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7],  # right-down
            [-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7],  # left-up
            [-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7]  # left-down
        ]


class Queen(Piece):
    image = ('♕', '♛')

    def get_moves(self):
        return [
            [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0],  # right
            [-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0],  # left
            [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7],  # up
            [0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7],  # down
            [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7],  # right-up
            [1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7],  # right-down
            [-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7],  # left-up
            [-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7]  # left-down
        ]


class King(Piece):
    image = ('♔', '♚')

    def get_moves(self):
        return [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
