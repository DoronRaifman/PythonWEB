from enum import Enum


class PieceColor(Enum):
    White = 1
    Black = 2


class PieceType(Enum):
    Pawn = 1
    Bishop = 2
    Knight = 3
    Rook = 4
    Queen = 5
    King = 7
