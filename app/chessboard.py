from app.pieces import Color, Empty, Pawn, Rook, Knight, Bishop, Queen, King


class Chessboard(object):
    def __init__(self):
        self.board = [
            [Rook(Color.BLACK), Knight(Color.BLACK), Bishop(Color.BLACK), Queen(Color.BLACK), King(Color.BLACK), Bishop(Color.BLACK), Knight(Color.BLACK), Rook(Color.BLACK)],
            [Pawn(Color.BLACK), Pawn(Color.BLACK), Pawn(Color.BLACK), Pawn(Color.BLACK), Pawn(Color.BLACK), Pawn(Color.BLACK), Pawn(Color.BLACK), Pawn(Color.BLACK)],
            [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
            [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
            [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
            [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
            [Pawn(Color.WHITE), Pawn(Color.WHITE), Pawn(Color.WHITE), Pawn(Color.WHITE), Pawn(Color.WHITE), Pawn(Color.WHITE), Pawn(Color.WHITE), Pawn(Color.WHITE)],
            [Rook(Color.WHITE), Knight(Color.WHITE), Bishop(Color.WHITE), Queen(Color.WHITE), King(Color.WHITE), Bishop(Color.WHITE), Knight(Color.WHITE), Rook(Color.WHITE)]
        ]

    def __repr__(self):
        res = ''
        for i in range(8):
            for j in range(8):
                res += ' ' + self.board[i][j].__str__()
            res += "\n"
        return res
