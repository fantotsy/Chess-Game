class Color(object):
    EMPTY = 0
    WHITE = 1
    BLACK = 2


class Piece(object):
    image = None

    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return self.image[0 if self.color == Color.BLACK else 1]


class Empty(object):
    color = Color.EMPTY

    def __repr__(self):
        return '.'


class Pawn(Piece):
    image = ('♙', '♟')


class Rook(Piece):
    image = ('♖', '♜')


class Knight(Piece):
    image = ('♘', '♞')


class Bishop(Piece):
    image = ('♗', '♝')


class Queen(Piece):
    image = ('♕', '♛')


class King(Piece):
    image = ('♔', '♚')
