import numpy as np
import pygame
import sys
import math
import random

NO_OF_ROWS = 6
NO_OF_COLUMNS = 7

player = 0
AI = 1

blue = (0, 0, 255)
black = (0, 0 ,0)
red = (255, 0, 0)
yellow = (255, 255, 0)

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

#flipping board
def print_board(board):
    print(np.flip(board,0))

def draw_board(board):
    for c in range(NO_OF_COLUMNS):
        for r in range(NO_OF_ROWS):
            pygame.draw.rect(screen, blue, (c * square_size, r * square_size + square_size, square_size, square_size))
            pygame.draw.circle(screen, black, (c * square_size + square_size / 2, r * square_size + square_size + square_size / 2), radius)

    for c in range(NO_OF_COLUMNS):
        for r in range(NO_OF_ROWS):
            if board[r][c] == 1:
                pygame.draw.circle(screen, red, (int(c * square_size + square_size/2), height-int(r * square_size + square_size/2)), radius)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, yellow, (int(c * square_size + square_size/2), height-int(r * square_size + square_size / 2)), radius)
    pygame.display.update()

board = create_board()
print_board(board)

game_over = False
turn = player

pygame.init()

square_size = 100
width = square_size * NO_OF_COLUMNS
height = square_size * (NO_OF_ROWS + 1)
size = (width, height)
radius = int(square_size/2 - 5)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, black, (0,0, width, square_size))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, red, (posx, int(square_size / 2)), radius)
            else:
                pygame.draw.circle(screen, yellow, (posx, int(square_size / 2)), radius)
        pygame.display.update()

    if event.type == pygame.MOUSEBUTTONDOWN:
        pygame.draw.rect(screen, black, (0,0, width, square_size))

        if turn == 0:

            posx = event.pos[0]
            col = int(math.floor(posx/square_size))

                # while True:
                    # col = int(input("Player 1's turn, select a value between 0-6:"))
                    # if col < 0 or col > 6:
                    #     print("Invalid Move. Please select a value between 0 and 6.")
                    # else:
                    #     break

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)

                if winning_move(board, 1):
                        # print_board(board)
                    label = myfont.render("Player 1 wins!!", 1, red)
                    screen.blit(label, (40,10))
                    print("Player 1 Wins!")
                    game_over = True

                turn += 1
                turn = turn % 2
                print_board(board)
                draw_board(board)

    #player 2 AI
    if turn == AI and not game_over:
        col = random.randint(0, NO_OF_COLUMNS - 1)

        if is_valid_location(board, col):
            pygame.time.wait(500)
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

            if winning_move(board, 2):
                # print_board(board)
                label = myfont.render("Player 2 wins!!", 1, yellow)
                screen.blit(label, (40,10))
                print("Player 2 Wins!")
                game_over = True

            print_board(board)
            draw_board(board)

        turn += 1
        turn = turn % 2

    if game_over:
        pygame.time.wait(2000)

