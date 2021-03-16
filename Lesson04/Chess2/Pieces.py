from Lesson04.Chess2.Enums import PieceColor, PieceType
from Lesson04.Chess2.PieceBase import PieceBase


class PiecePawn(PieceBase):
    def __init__(self, board, row: int, col: int, piece_color: PieceColor):
        super().__init__(board, row, col, PieceType.Pawn, piece_color)


class PieceRook(PieceBase):
    def __init__(self, board, row: int, col: int, piece_color: PieceColor):
        super().__init__(board, row, col, PieceType.Rook, piece_color)

    def get_all_theoretical_possible_moves(self):
        return self.get_all_strait_possible_moves()


class PieceKnight(PieceBase):
    def __init__(self, board, row: int, col: int, piece_color: PieceColor):
        super().__init__(board, row, col, PieceType.Knight, piece_color)
        self.is_can_skip_pieces = True

    def get_all_theoretical_possible_moves(self):
        # deltas = [(2, -1), (2, 1), (-2, -1), (-2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        values1, values2 = [1, -1], [2, -2]
        deltas = [(i, j) for i in values2 for j in values1] + [(j, i) for i in values2 for j in values1]
        possible_moves = {}
        row, col = self.get_position()
        for i, delta in enumerate(deltas):
            delta_row, delta_col = delta
            if self.is_legal_position(row + delta_row, col + delta_col):
                possible_moves[i] = (row + delta_row, col + delta_col)
        return  possible_moves


class PieceBishop(PieceBase):
    def __init__(self, board, row: int, col: int, piece_color: PieceColor):
        super().__init__(board, row, col, PieceType.Bishop, piece_color)

    def get_all_theoretical_possible_moves(self):
        return self.get_all_diagonal_possible_moves()


class PieceQueen(PieceBase):
    def __init__(self, board, row: int, col: int, piece_color: PieceColor):
        super().__init__(board, row, col, PieceType.Queen, piece_color)

    def get_all_theoretical_possible_moves(self):
        strait_moves = self.get_all_strait_possible_moves()
        diagonal_moves = self.get_all_diagonal_possible_moves()
        moves = strait_moves.copy()
        moves.update(diagonal_moves)
        return moves


class PieceKing(PieceBase):
    def __init__(self, board, row: int, col: int, piece_color: PieceColor):
        super().__init__(board, row, col, PieceType.King, piece_color)

    def get_all_theoretical_possible_moves(self):
        # deltas = [(1, -1), (1, 1), (-1, -1), (-1, 1), (1, 0), (-1, 0), (0, -1), (0, 1)]
        values = [1, -1]
        deltas = [(i, j) for i in values for j in values] + [(i, 0) for i in values] + [(0, i) for i in values]
        possible_moves = {}
        row, col = self.get_position()
        for i, delta in enumerate(deltas):
            delta_row, delta_col = delta
            if self.is_legal_position(row + delta_row, col + delta_col):
                possible_moves[i] = (row + delta_row, col + delta_col)
        return  possible_moves



