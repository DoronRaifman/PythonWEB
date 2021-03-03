import copy
from Lesson3.Chess.Enums import PieceColor, PieceType
from Lesson3.Chess.PieceBase import PieceBase


class Board:
    def __init__(self):
        self.board = {
            (row, col): None for row in range(1, 9) for col in range(1, 9)}
        self.killed_peaces_white = []
        self.killed_peaces_black = []

    def get_piece(self, row, col):
        piece: PieceBase = self.board[(row, col)]
        return piece

    def move_piece(self, peace, row, col):
        peace: PieceBase = peace
        dest_piece = self.get_piece(row, col)
        if dest_piece is not None:
            dest_piece.board = None
            if dest_piece.piece_color:
                self.killed_peaces_white.append(dest_piece)
            else:
                self.killed_peaces_black.append(dest_piece)
        self.board[(row, col)] = peace

    def fill_initial_board(self):
        # empty board
        self.board = {(row, col): None for row in range(1, 9) for col in range(1, 9)}
        board_officers_data = [
            # officers (col, peace_type)
            (1, PieceType.Rook), (8, PieceType.Rook),
            (2, PieceType.Knight), (7, PieceType.Knight),
            (3, PieceType.Bishop), (6, PieceType.Bishop),
            (4, PieceType.Queen), (5, PieceType.King),
        ]
        for officer in board_officers_data:
            col, piece_type = officer
            self.board[(1, col)] = PieceBase.piece_factory(
                self, 1, col, piece_type, PieceColor.White)
            self.board[(8, col)] = PieceBase.piece_factory(
                self, 8, col, piece_type, PieceColor.White)

        pones_white = [(2, col, PieceType.Pawn, PieceColor.White) for col in range(1, 9)]
        pones_black = [(7, col, PieceType.Pawn, PieceColor.Black) for col in range(1, 9)]
        for pone in pones_white + pones_black:
            row, col, piece_type, piece_color = pone
            self.board[(row, col)] = PieceBase.piece_factory(
                self, row, col, piece_type, piece_color)

    def get_board_copy(self):
        new_board = copy.deepcopy(self)
        for peace in self.board.values():
            if peace is not None:
                peace.board = new_board
        return new_board

