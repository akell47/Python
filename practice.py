# # take weighted average of dictionary keys
# this section takes a weighted average of dictionaries with float key arrays
# from random import randint
# print "Random Number"
# print(randint(0,100))
#
# dictionary1 = {
#     "name"       : "Dictionary1",
#     "numbersetA" : [21.0, 66.0, 39.0],
#     "numbersetB" : [13.0, 22.0, 60.0, 55.0],
#     "numbersetC" : [22.0, 85.0]
# }
#
# dictionary2 = {
#     "name"       : "Dictionary2",
#     "numbersetA" : [23.0, 17.0, 49.0],
#     "numbersetB" : [37.0, 92.0, 82.0, 53.0],
#     "numbersetC" : [13.0, 43.0]
# }
#
# def average(numbers):
#     total = float(sum(numbers))
#     return total / len(numbers)
#
# print "Dictionary 1 Set A average"
# print average(dictionary1["numbersetA"])
# print "Dictionary 2 Set A average"
# print average(dictionary1["numbersetA"])
#
# def get_weighted_average(dictionary):
#     A = average(dictionary["numbersetA"])
#     B = average(dictionary["numbersetB"])
#     C = average(dictionary["numbersetC"])
#     return 0.1 * A + 0.3 * B + 0.6
#
# print "Average of Dictionary 1"
# print get_weighted_average(dictionary1)
# print "Average of Dictionary 2"
# print get_weighted_average(dictionary2)
#
# dictionaries = [dictionary1, dictionary2]
#
# def get_whole_average(dictionaries):
#     results = []
#     for dictionary in dictionaries:
#         x = get_weighted_average(dictionary)
#         results.append(x)
#     return average(results)
#
# print "Average of Dictionaries 1 and 2 with weighted average"
# print get_whole_average(dictionaries)

n = [1, 3, 5]
print n
def total(numbers):
    result = 0
    for item in numbers:
        result = result + item
    return result
print "total"
print total(n)
x = n[1] * 5
n[1] = x
print n
def total(numbers):
    result = 0
    for item in numbers:
        result = result + item
    return result
print "total"
print total(n)
n.append(4)
print n
# should be [1, 15, 5, 4]
a = n[0]
n.remove(a)
print n
# should be [15 ,5, 4] at this point
def print_it_yo(doityo):
    return doityo
print print_it_yo(n)
# same thing, should be [15, 5, 4] again :)
def first_item(x):
    return x[0]
print first_item(n)
# should be [15]
def double_first(x):
    return x[0] * 2
print double_first(n)
# 30
print "n"
print n
def append_nine(x):
    x.append(9)
    return x
print append_nine(n)
# [15, 5, 4 ,9]
def print_each(x):
    for i in range(0, len(x)):
        print x[i]
print_each(n)
def double_each(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x
print double_each(n)
# [30, 10, 8, 18 ]
def total(numbers):
    result = 0
    for item in numbers:
        result = result + item
    return result
print "total"
print total(n)
# # def double_each2(x):
# #     for i in range(0, len(x)):
# #         x[i] = x[i] * 2
# #         print x[i]
# # print double_each2(n)
print "range practice start"
print range(10)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print range(5,11)
# [5, 6, 7, 8, 9, 10]
print range(0,10,2)
# [0, 2, 4, 6, 8]
print double_each(range(10))
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print double_each(range(0,10,2))
# [0, 4, 8, 12, 16]
print double_each(range(0,3,1))
# [0, 2, 4]
for x in range(5):
    print x
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
