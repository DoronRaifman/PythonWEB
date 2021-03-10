from Lesson4.Chess.Enums import PieceColor, PieceType
from Lesson4.Chess.PieceBase import PieceBase


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
        deltas = [(2, -1), (2, 1), (-2, -1), (-2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        possible_moves = {1: []}
        row, col = self.get_position()
        for delta in deltas:
            delta_row, delta_col = delta
            if self.is_legal_position(row + delta_row, col + delta_col):
                possible_moves[1].append((row + delta_row, col + delta_col))
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
        deltas = [(1, -1), (1, 1), (-1, -1), (-1, 1), (1, 0), (-1, 0), (0, -1), (0, 1)]
        possible_moves = {1: []}
        row, col = self.get_position()
        for delta in deltas:
            delta_row, delta_col = delta
            if self.is_legal_position(row + delta_row, col + delta_col):
                possible_moves[1].append((row + delta_row, col + delta_col))
        return  possible_moves



