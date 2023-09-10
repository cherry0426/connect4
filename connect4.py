import numpy as np

def create_board():
    #creating a board of size 6 x 7
    board = np.zeros((6,7))
    return(board)

print(create_board())