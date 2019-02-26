from app.pieces import Color, Empty, Pawn, Rook, Knight, Bishop, Queen, King


class Chessboard(object):
    x_position_to_index = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7
    }

    index_to_x_position = {
        0: 'a',
        1: 'b',
        2: 'c',
        3: 'd',
        4: 'e',
        5: 'f',
        6: 'g',
        7: 'h'
    }

    def __init__(self):
        self.board = [
            [Rook(Color.WHITE), Pawn(Color.WHITE), Empty(), Empty(), Empty(), Empty(), Pawn(Color.BLACK), Rook(Color.BLACK)],
            [Knight(Color.WHITE), Pawn(Color.WHITE), Empty(), Empty(), Empty(), Empty(), Pawn(Color.BLACK), Knight(Color.BLACK)],
            [Bishop(Color.WHITE), Pawn(Color.WHITE), Empty(), Empty(), Empty(), Empty(), Pawn(Color.BLACK), Bishop(Color.BLACK)],
            [Queen(Color.WHITE), Pawn(Color.WHITE), Empty(), Bishop(Color.WHITE), Empty(), Empty(), Pawn(Color.BLACK), Queen(Color.BLACK)],
            [King(Color.WHITE), Pawn(Color.WHITE), Empty(), Empty(), Bishop(Color.BLACK), Empty(), Pawn(Color.BLACK), King(Color.BLACK)],
            [Bishop(Color.WHITE), Pawn(Color.WHITE), Empty(), Empty(), Empty(), Empty(), Pawn(Color.BLACK), Bishop(Color.BLACK)],
            [Knight(Color.WHITE), Pawn(Color.WHITE), Empty(), Empty(), Empty(), Empty(), Pawn(Color.BLACK), Knight(Color.BLACK)],
            [Rook(Color.WHITE), Pawn(Color.WHITE), Empty(), Empty(), Empty(), Empty(), Pawn(Color.BLACK), Rook(Color.BLACK)]
        ]

    def get_targets(self, position):
        x_position = self.x_position_to_index[position[0]]  # x position is from left to right
        y_position = int(position[1]) - 1  # y position is from down to up

        piece = self.board[x_position][y_position]
        moves = piece.get_moves()

        result = []
        for single_direction_moves in moves:
            for single_direction_move in single_direction_moves:
                x_target = x_position + single_direction_move[0]
                y_target = y_position + single_direction_move[1]
                if 0 <= x_target <= 7 and 0 <= y_target <= 7:
                    target_piece = self.board[x_target][y_target]
                    if target_piece.color != piece.color:
                        result.append(self.index_to_x_position[x_target] + str(y_target + 1))
                    if target_piece.color != Color.EMPTY:
                        break

        return result

    def perform_movement(self, position, target):
        x_position = self.x_position_to_index[position[0]]  # x position is from left to right
        y_position = int(position[1]) - 1  # y position is from down to up
        x_target = self.x_position_to_index[target[0]]  # x position is from left to right
        y_target = int(target[1]) - 1  # y position is from down to up

        self.board[x_target][y_target] = self.board[x_position][y_position]
        self.board[x_position][y_position] = Empty()

        return
