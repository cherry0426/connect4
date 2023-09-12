import numpy as np

NO_OF_ROWS = 6
NO_OF_COLUMNS = 7

def create_board():
    #creating a board of size 6 x 7
    board = np.zeros((6,7))
    return(board)

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[5][col] == 0

def get_next_open_row(board, col):
    for r in range(NO_OF_ROWS):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board,0))

board = create_board()
print_board(board)

game_over = False
turn = 0

while not game_over:
    #player 1
    if turn == 0:
        col = int(input("Player 1's turn, select a value between 0-6:"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

    #player 2
    else:
        col = int(input("Player 2's turn, select a value between 0-6:"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

    turn += 1
    turn = turn % 2

    print_board(board)

