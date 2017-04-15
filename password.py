print "I'm \n working"

import random

print "random number between 1 and 4 is:",random.choice([1,2,3,4])
print "random letter from 'abcdef is:",random.choice("abcdef")

def password(length):
    pw = str()
    char = "abcdefghijklmnopqrstuvwzyz" + "0123456789"
    for i in range(length):
        pw = pw + random.choice(char)
    return pw

print "password of 10 characters is :",password(10)








