# While loop
# similar to if - execute code inside of loop if some condition is true
# while continue to execute as long as the condition is true
# not if its true, while it is true
#
# count = 0
#
# if count <= 5:
#     print "the if statement says:", count
#
# while count <=5:
#     print "the while statement says", count
#     # need =+ so that it is not an infinite loop
#     count += 1
#
# loop_condition = True
#
# while loop_condition:
#     print "I'm Loopy, the loop"
#     loop_condition = False

# square numbers 1 to 10
# num = 1

# while num <= 10:
#     print num ** 2
#     num += 1

# while True:
#     print num
#     num += 1
#     if num >= 10:
#         # while statement is always true which creates an infinate loop
#         # break stops the infinate loop - if number is greater or equal to 10
#         break

# while/else
# unique to Python - the else block will execute ANYTIME the loop is evaluated
# be False.  - will be executed weather or not the loop is entered or exits normally
# if loop exits b/c of break the else will not be executed
import random

# print "four numbers will come out"
# print "if there is a 5 or 3 = you loose"
#
# count = 0
# while count < 4:
#     num = random.randint(1,6)
#     print num
#     if num == 5 or num == 3:
#         print "lost"
#         break
#     count += 1
# else:
#     print "no 3 or 5 so you win"

# from random import randint
# # random number is generated
# random_number = randint(1,10)
# # game to guess what the random number is
# # print random_number
# guesses_left = 3
#
# while guesses_left > 0:
#     guess = int(raw_input("Guess a number between 1 and 10"))
#     if guess == random_number:
#         print "you win"
#         break
#     guesses_left -= 1
# else:
#     print "you loose"

# loop over dicitonary
dictionary = {
"a" : "apple",
"b" : "berry",
"c" : "cherry"
}

for key in dictionary:
    print key, dictionary[key]

for thing, things in enumerate(dictionary):
    print thing + 1, things
