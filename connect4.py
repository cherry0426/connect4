import numpy as np

NO_OF_ROWS = 6
NO_OF_COLUMNS = 7

def create_board():
    #creating a board of size 6 x 7
    board = np.zeros((NO_OF_ROWS, NO_OF_COLUMNS))
    return(board)

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[5][col] == 0

def get_next_open_row(board, col):
    for r in range(NO_OF_ROWS):
        if board[r][col] == 0:
            return r

def winning_move(board, piece):
    #horizontal check
    for c in range(NO_OF_COLUMNS - 3):
        for r in range(NO_OF_ROWS):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return(True)

    #vertical check
    for c in range(NO_OF_COLUMNS):
        for r in range(NO_OF_ROWS - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return(True)

    #check for postive diagonals
    for c in range(NO_OF_COLUMNS - 3):
        for r in range(NO_OF_ROWS - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return(True)

    #check for negative diagonals
    for c in range(NO_OF_COLUMNS - 3):
        for r in range(3, NO_OF_ROWS):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return(True)


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

            if winning_move(board, 1):
                print_board(board)
                print("Player 1 Wins!")
                game_over = True
                quit()

        turn  = 1

    #player 2
    else:
        col = int(input("Player 2's turn, select a value between 0-6:"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

            if winning_move(board, 2):
                print_board(board)
                print("Player 2 Wins!")
                game_over = True
                quit()

        turn = 0

    print_board(board)

