import random
import numpy as np

def create_board():
    board = np.zeros((3,3), dtype=int)
    return board

board = create_board()
print (board)

def place(board, player, position):
    if player not in [1,2]:
        raise ValueError("Your player can only be 1 or 2")
    x = position[0]
    y = position[1]
    # print("x",x)
    # print("y",y)
    if x < 3 and y < 3:
        board[x,y] = player
        return board
    else:
        raise ValueError("Your position is off the board.")

def possibilities(board):
    possible = np.where(board == 0)
    return zip(possible[0],possible[1])

def random_place(board, player):
    # get all the possibilities
    # find a random one
    possibleplaces = possibilities(board)
    selection = random.choice(possibleplaces)
    return place(board, player, selection)

# print ("random_place",(random_place(board, 2)))

for i in range(4):
    for player in [1, 2]:
        random_place(board, player)
        #print "player", player

# print (board)
# print ("possibilities",(possibilities(board)))

def row_win(board, player):
    ind = [0,1,2]
    winstatus = False
    for rowindex in ind:
        # print (board[rowindex])
        if (board[rowindex] == player).sum() == len(board[0]):
            winstatus = True
    return winstatus

# print "row win:",(row_win(board,player))
# print "row win 1:",(row_win(board, 1))
# print "row win 2:",(row_win(board, 2))

def col_win(board, player):
    row_flip = np.transpose(board)
    winstatus = False
    cols = [0,1,2]
    for colindex in cols:
        # print row_flip[colindex]
        if (row_flip[colindex] == player).sum() == len(row_flip[0]):
            winstatus = True
    return winstatus


# print ("column win:",(col_win(board, player)))
# print ("column win 1:",(col_win(board, 1)))
# print ("column win 2:",(col_win(board, 2)))

def diag_win(board, player):
    if np.all(np.diagonal(board) == player):
        return True
    Other_diag = np.fliplr(board)
    if np.all(np.diagonal(Other_diag) == player):
        return True
    else:
        return False

# print ("diagonal win:",(diag_win(board, player)))
# print ("diagonal win 1:",(diag_win(board, 1)))
# print ("diagonal win 2:",(diag_win(board, 2)))

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # Check if `row_win`, `col_win`, or `diag_win` apply.  if so, store `player` as `winner`.
        if row_win(board,player) == True:
            winner = player
        elif col_win(board,player) == True:
            winner = player
        elif diag_win(board,player) == True:
            winner = player
    return winner
    if np.all(board != 0) and winner == 0:
        winner = -1
        return winner

# print ("WINNER IS:",(evaluate(board)))
print "------"

def play_game():
    board = create_board()
    for i in range(3):
        for player in [1, 2]:
            random_place(board, player)
            evaluation = evaluate(board)
    return evaluation

import time

start_time = time.clock()
games = [play_game() for i in range(10)]
end_time = time.clock()
print start_time - end_time
print games


def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            # use `random_place` to play a game, and store as `board`.
            # use `evaluate(board)`, and store as `winner`.
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

print "strategic game",play_strategic_game()

strategic_games = [play_strategic_game() for i in range(10)]
print strategic_games
