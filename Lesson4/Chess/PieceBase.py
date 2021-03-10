from Lesson4.Chess.Enums import PieceColor, PieceType
import Lesson4.Chess.Board as brd

class PieceBase:
    def __init__(self, board, row:int, col:int, piece_type:PieceType,
                 piece_color:PieceColor):
        self.row, self.col = row, col
        self.piece_type:PieceType = piece_type
        self.piece_color:PieceColor = piece_color
        self.board:brd.Board = board
        self.is_can_skip_pieces = False

    def __str__(self):
        return f'{self.piece_type.name}, {self.piece_color.name}, ({self.row}, {self.col})'

    def __repr__(self):
        return str(self)

    def set_position(self, row, col):
        self.row, self.col = row, col

    def get_position(self):
        return (self.row, self.col)

    def is_legal_position(self, row, col):
        return 1 <= row <= 8 and 1 <= col <= 8

    def is_hit_move(self, row, col):
        piece = self.get_piece(row, col)
        return piece is not None and piece.piece_color != self.piece_color

    def is_move_or_hit_possible(self, row, col):
        # Todo: implement
        return False

    """
    methods that use Board
    """
    def get_piece(self, row, col):
        return self.board.get_piece(row, col)

    """
    methods that must be implemented in the derived class
    """
    def is_move_possible(self, row, col):
        raise Exception("Don't call me")

    def is_can_hit(self, row, col):
        raise Exception("Don't call me")

    def get_all_theoretical_possible_moves(self):
        # return all theoretical possible moves to all directions
        #   ignore existing pieces
        # return dict of list of tuples {1: [(row, col)]}
        # return {1: [(0, 0)], 2:[(1, 0)]}
        raise Exception("Don't call me")

    def get_icon_name(self):
        raise Exception("Don't call me")

    """
    some possible moves building blocks
    """
    def get_all_strait_possible_moves(self):
        possible_moves = {}
        row, col = self.get_position()
        possible_moves[1] = [(row, col) for row in range(row+1, 9)]
        if row > 1:
            moves = [(row, col) for row in range(1, row - 1)]
            possible_moves[2] = moves[::-1]
        possible_moves[3] = [(row, col) for col in range(col+1, 9)]
        if col > 1:
            moves = [(row, col) for col in range(1, col - 1)]
            possible_moves[4] = moves[::-1]
        return possible_moves

    def get_all_diagonal_possible_moves(self):
        possible_moves = {i: [] for i in range(5, 5+4+1)}
        row, col = self.get_position()
        for delta in range(1, 8):
            if self.is_legal_position(row+delta, col+delta):
                possible_moves[5].append((row+delta, col+delta))
            if self.is_legal_position(row-delta, col-delta):
                possible_moves[6].append((row-delta, col-delta))
            if self.is_legal_position(row+delta, col-delta):
                possible_moves[7].append((row+delta, col-delta))
            if self.is_legal_position(row-delta, col+delta):
                possible_moves[8].append((row-delta, col+delta))
        return possible_moves

    """
    Piece factory
    """
    @staticmethod
    def piece_factory(board, row:int, col:int,
                      piece_type:PieceType, piece_color:PieceColor):
        import Lesson4.Chess.Pieces as pcs

        piece = None
        if piece_type == PieceType.Pawn:
            piece = pcs.PiecePawn(board, row, col, piece_color)
        elif piece_type == PieceType.Rook:
            piece = pcs.PieceRook(board, row, col, piece_color)
        elif piece_type == PieceType.Knight:
            piece = pcs.PieceKnight(board, row, col, piece_color)
        elif piece_type == PieceType.Bishop:
            piece = pcs.PieceBishop(board, row, col, piece_color)
        elif piece_type == PieceType.Queen:
            piece = pcs.PieceQueen(board, row, col, piece_color)
        elif piece_type == PieceType.King:
            piece = pcs.PieceKing(board, row, col, piece_color)
        return piece

