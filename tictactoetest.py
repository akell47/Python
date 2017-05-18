import random
import numpy as np

def create_board():
    board = np.zeros((3,3), dtype=int)
    return board

def place(board, player, position):
    if player not in [1,2]:
        raise ValueError("Your player can only be 1 or 2")
    x = position[0]
    y = position[1]
    # print(x)
    # print(y)
    if x < 3 and y < 3:
        board[x,y] = player
        return board
    else:
        raise ValueError("Your position is off the board.")

# board = create_board()
# place(board, 2, (1,1))

# print (board)

# def possibilities(board):
#     possible = np.where(board == 0)
#     return zip(possible[0],possible[1])

# print (possibilities(board))

# def random_place(board, player):
#     # get all the possibilities
#     # find a random one
#     possibleplaces = possibilities(board)
#     selection = random.choice(possibleplaces)
#     return place(board, player, selection)

# print (random_place(board, 2))


board = create_board()
# for i in range(3):
#     for player in [1, 2]:
#         random_place(board, player)

print (board)

place(board, 1, (0,0))
place(board, 1, (0,1))
place(board, 1, (0,2))
# place(board, 2, (1,0))
#place(board, 1, (0,2))
place(board, 1, (1,1))
place(board, 1, (2,1))
# place(board, 2, (1,2))
print (board)

def row_win(board, player):
    ind = [0,1,2]
    winstatus = False
    for rowindex in ind:
        # print (board[rowindex])
        if (board[rowindex] == player).sum() == len(board[0]):
            winstatus = True
    return winstatus

print "row_win ONE:",(row_win(board, 1))
print "-------"

def col_win(board, player):
    row_flip = np.transpose(board)
    winstatus = False
    cols = [0,1,2]
    for colindex in cols:
        # print row_flip[colindex]
        if (row_flip[colindex] == player).sum() == len(row_flip[0]):
            winstatus = True
    return winstatus


print "col_win player ONE:",(col_win(board, 1))

def diag_win(board, player):
    if np.all(np.diagonal(board) == player):
        return True
    Other_diag = np.fliplr(board)
    if np.all(np.diagonal(Other_diag) == player):
        return True
    else:
        return False

# print "diag_win 1:",(diag_win(board, 1))

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # Check if `row_win`, `col_win`, or `diag_win` apply.  if so, store `player` as `winner`.
        if row_win(board, player) == True:
            return player
        elif col_win(board, player) == True:
            player = winner
        elif diag_win(board, player) == True:
            player = winner
        return winner
    if np.all(board != 0) and winner == 0:
        winner = -1
        return winner

print ("WINNER IS:",(evaluate(board)))












# my_board = create_board()
# player = 1
# while len(possibilities(board)) > 0:
#     pos = raw_input("Choose a position!")
#     place(my_board, player, pos)
#     print my_board
#     if player == 1:
#         player = 2
#     elif player == 2:
#         player = 1
#     else:
#         raise ValueError("Something happened with the number of players!")
