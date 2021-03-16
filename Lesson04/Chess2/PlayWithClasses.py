from Lesson04.Chess2.Board import Board


def print_board(board):
    pieces_by_row_col = {}
    for pos, piece in board.items():
        if piece is not None:
            row, col = pos
            if row not in pieces_by_row_col:
                pieces_by_row_col[row] = {}
            pieces_by_row_col[row][col] = piece
    for row, row_dict in pieces_by_row_col.items():
        col_keys_sorted = sorted(row_dict.keys())
        line = f'row {row}: '
        for col in col_keys_sorted:
            piece = row_dict[col]
            line += f'{col}:{str(piece)}, '
        print(f'{line[:-2]}')


def print_moves(piece, moves):
    print(repr(piece))
    for direction, move_positions in moves.items():
        line = f'direction {direction}: '
        for position in move_positions:
            row, col = position
            line += f'({row}, {col}),'
        print(line)


if __name__ == '__main__':
    board = Board()
    board.fill_initial_board()
    # print_board(board.board)

    piece = board.get_piece(2, 5)
    board.move_piece(piece, 4, 5)
    print_board(board.board)

    piece = board.get_piece(1, 6)
    moves = piece.get_all_theoretical_possible_moves()
    print_moves(piece, moves)

    piece = board.get_piece(1, 4)
    moves = piece.get_all_theoretical_possible_moves()
    print_moves(piece, moves)

