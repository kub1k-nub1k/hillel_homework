import random

def generate_chessboard():

    chess_pieces = ['♕', '♖', '♗', '♘', '♙', '♚', '♛', '♜', '♝', '♞', '♟']

    chessboard = [[' ' for _ in range(8)] for _ in range(8)]

    for i in range(8):
        for j in range(8):
            if random.random() <= 0.08:
                chessboard[i][j] = random.choice(chess_pieces)

    return chessboard

def print_chessboard(chessboard):
    colors = ['\x1b[47m', '\x1b[100m']

    cell_width = 3

    red_color = '\x1b[31m'

    top_row = red_color + '     a  b  c  d  e  f  g  h' + '\x1b[0m'
    print(top_row)

    for i, row in enumerate(chessboard, 1):
        row_number = str(i)
        row_number = red_color + row_number.center(cell_width) + '\x1b[0m'
        row_str = f'{row_number} '

        for j, piece in enumerate(row):
            color_code = colors[(i + j) % 2]
            cell = f'{color_code}{piece.center(cell_width)}\x1b[0m'
            row_str += cell

        print(row_str)


if __name__ == "__main__":
    chessboard = generate_chessboard()
    print_chessboard(chessboard)
