import copy
from Lesson04.Chess1.Enums import PieceColor, PieceType
import Lesson04.Chess1.PieceBase as pb


class Board:
    def __init__(self):
        self.board = {
            (row, col): None for row in range(1, 9) for col in range(1, 9)}
        self.killed_peaces_white = []
        self.killed_peaces_black = []

    def get_piece(self, row, col):
        piece: pb.PieceBase = self.board[(row, col)]
        return piece

    def move_piece(self, peace, row, col):
        peace: pb.PieceBase = peace
        self.board[(peace.row, peace.col)] = None
        peace.set_position(row, col)
        dest_piece = self.get_piece(row, col)
        if dest_piece is not None:
            dest_piece.board = None
            if dest_piece.piece_color == PieceColor.White:
                self.killed_peaces_white.append(dest_piece)
            else:
                self.killed_peaces_black.append(dest_piece)
        self.board[(row, col)] = peace

    def fill_initial_board(self):
        # empty board
        self.board = {(row, col): None for row in range(1, 9) for col in range(1, 9)}
        board_officers_data = [
            # officers (col, pieace_type)
            (1, PieceType.Rook), (8, PieceType.Rook),
            (2, PieceType.Knight), (7, PieceType.Knight),
            (3, PieceType.Bishop), (6, PieceType.Bishop),
            (4, PieceType.Queen), (5, PieceType.King),
        ]
        for officer in board_officers_data:
            col, piece_type = officer
            self.board[(1, col)] = pb.PieceBase.piece_factory(
                self, 1, col, piece_type, PieceColor.White)
            self.board[(8, col)] = pb.PieceBase.piece_factory(
                self, 8, col, piece_type, PieceColor.Black)

        pones_white = [(2, col, PieceType.Pawn, PieceColor.White) for col in range(1, 9)]
        pones_black = [(7, col, PieceType.Pawn, PieceColor.Black) for col in range(1, 9)]
        for pone in pones_white + pones_black:
            row, col, piece_type, piece_color = pone
            self.board[(row, col)] = pb.PieceBase.piece_factory(
                self, row, col, piece_type, piece_color)

    def get_board_copy(self):
        new_board = Board()
        for piece in self.board.values():
            if piece is not None:
                row, col = piece.row, piece.col
                piece_new: pb.PieceBase = copy.copy(piece)
                piece_new.board = new_board
                new_board.board[(row, col)] = piece_new
        return new_board

