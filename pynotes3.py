def is_even(x):
    if x%2 == 0:
        return True
    elif x%2 == 1:
        return False

x = 4
print is_even(x)
y = 5
print is_even(y)

def is_int(x):
    if type(x) == int:
        return True
# returns true for numbers with .0 as decimal place so they are considered intigers too
    elif x%1 == 0:
        return True
    else:
        return False
a = 3.3
print is_int(a)
b = 4
print is_int(b)
c = 4.0
print is_int(c)
#
# def is_prime(x):
#     x = abs(x)
#     if x > 1:
#         for i in range(2, x):
#             if x % abs(i) == 0:
#                 retrun False
#                 break
#     elif x == 1 or x == 0:
#         return False
#
# print b, is_prime(b)

print "10 / 20"
A = float(10)/20
print A

# print sentence as an array
phrase = "the mouse went up the clock"
phrase_list = phrase.split()
print phrase_list

# count words in a string
len(phrase_list)

# count characters in each word in phrase
for word in phrase_list:
    print len(word)
