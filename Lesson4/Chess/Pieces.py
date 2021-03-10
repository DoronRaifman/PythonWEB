from Lesson4.Chess.Enums import PieceColor, PieceType
from Lesson4.Chess.PieceBase import PieceBase


class PiecePawn(PieceBase):
    def __init__(self, board, row: int, col: int, piece_color: PieceColor):
        super().__init__(board, row, col, PieceType.Pawn, piece_color)


class PieceRook(PieceBase):
    def __init__(self, board, row: int, col: int, piece_color: PieceColor):
        super().__init__(board, row, col, PieceType.Rook, piece_color)


class PieceKnight(PieceBase):
    def __init__(self, board, row: int, col: int, piece_color: PieceColor):
        super().__init__(board, row, col, PieceType.Knight, piece_color)


class PieceBishop(PieceBase):
    def __init__(self, board, row: int, col: int, piece_color: PieceColor):
        super().__init__(board, row, col, PieceType.Bishop, piece_color)


class PieceQueen(PieceBase):
    def __init__(self, board, row: int, col: int, piece_color: PieceColor):
        super().__init__(board, row, col, PieceType.Queen, piece_color)


class PieceKing(PieceBase):
    def __init__(self, board, row: int, col: int, piece_color: PieceColor):
        super().__init__(board, row, col, PieceType.King, piece_color)


