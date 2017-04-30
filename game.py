output = []
# for y in range(5):
#     output.append(y)
#     print output
# for y in range(5):
#     output.append(["y"] * 5)
#     print output
for y in range(5):
    output.append(["(*)"] * 5)
    print output

def print_board(output):
    for line in output:
        # .join to get rid of quote marks and commas
        # " " the as the separator
        print "".join(line)
print "here"
print print_board(output)

from random import randint
def random_row(board):
    for o in board:
        return randint(0, len(board) -1)

def random_col(board):
    for o in board:
        return randint(0, len(board) -1)

place_row = random_row(output)
place_col = random_col(output)


print "Row is:"
print place_row
print "Column is"
print place_col

for turn in range(4):
    input_row = int(raw_input("Guess Row Number: "))
    input_col = int(raw_input("Guess Column Number: "))

    if input_row == place_row and input_col == place_col:
        print "Boom you got it! you WIN biiiach"
        break
    else:
        if input_row not in range(5) or input_col not in  range(5):
            print "Outta range fool! #facepalm!"
        elif output[input_row][input_col] == "(X)":
            print "dude guess something NEW, you guessed that one already!"
        else:
            print "You missed fool! muhaha"
            output[input_row][input_col] = "(X)"
            print_board(output)
            if turn == 3:
                print "Game Over out of turns"
        print "Turn", turn + 1
