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

def possibilities(board):
    possible = np.where(board == 0)
    return zip(possible[0],possible[1])

# print (possibilities(board))

def random_place(board, player):
    # get all the possibilities
    # find a random one
    possibleplaces = possibilities(board)
    selection = random.choice(possibleplaces)
    return place(board, player, selection)

# print (random_place(board, 2))


board = create_board()
for i in range(3):
    for player in [1, 2]:
        random_place(board, player)

print (board)














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
