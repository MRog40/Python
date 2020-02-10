# Michael Rogers
import matplotlib.pyplot as plt
import random

clear_board = [[0,0,0],
               [0,0,0],
               [0,0,0]]

board = clear_board
X_wins = 0
O_wins = 0

def play_games(games):
    X = 0
    O = 0
    for i in range(games+1):
        X1, O1 = play_game()
        X += X1
        O += O1
    print("X: " + X + " O: " + O + " Ties: " + (100-X-O))

def play_game():
    for i in range(10):
        if i % 2 is 0:
            place_piece(1)
        else:
            place_piece(4)
    board = clear_board
    if check_winner() % 2 is 0:
        return 1, 0 
    else:
        return 0, 1

def check_winner():
    #Check one way
    if board[0][0] + board[0][1] + board[0][2] is 3:
        return 1
    elif board[0][0] + board[0][1] + board[0][2] is 12:
        return 2

    elif board[1][0] + board[1][1] + board[1][2] is 3:
        return 1
    elif board[1][0] + board[1][1] + board[1][2] is 12:
        return 2

    elif board[2][0] + board[2][1] + board[2][2] is 3:
        return 1
    elif board[2][0] + board[2][1] + board[2][2] is 12:
        return 2
    #Check other way
    elif board[0][0] + board[1][0] + board[2][0] is 3:
        return 1
    elif board[0][0] + board[1][0] + board[2][0] is 12:
        return 2

    elif board[0][1] + board[1][1] + board[2][1] is 3:
        return 1
    elif board[0][1] + board[1][1] + board[2][1] is 12:
        return 2
    
    elif board[0][2] + board[1][2] + board[2][2] is 3:
        return 1
    elif board[0][2] + board[1][2] + board[2][2] is 12:
        return 2
    #Check diagonals
    elif board[0][0] + board[1][1] + board[2][2] is 3:
        return 1
    elif board[0][0] + board[1][1] + board[2][2] is 12:
        return 2
    elif board[2][0] + board[1][1] + board[0][2] is 3:
        return 1
    elif board[2][0] + board[1][1] + board[0][2] is 12:
        return 2
    else:
        return 0

def place_piece(num):
    x = random.randint(0,2)
    y = random.randint(0,2)

    while board[x][y] is not 0:
        x = random.randint(0,2)
        y = random.randint(0,2)

    board[x][y] = num

play_games(100)