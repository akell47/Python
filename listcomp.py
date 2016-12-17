nums = [1,2,3,4,5,6,7,8,9,10]

# print number for each number in nums
# "tradational" way- for loop way
a_list = []
for n in nums:
    a_list.append(n)
print a_list

# list comprehension
a_listcomp = [n for n in nums]
print a_listcomp

# print number * number for each number in nums
a_list2 = []
for n in nums:
    a_list2.append(n * n)
print a_list2

# list comprehension
a_list2comp = [n * n for n in nums]
print a_list2comp

# map and lambda way
a_list2lambda = map(lambda n: n*n, nums)
print a_list2lambda

# print number for each number if number is even
a_list3 = []
for n in nums:
    if n % 2 == 0:
        a_list3.append(n)
print a_list3

# list comprehension
a_list3comp = [n for n in nums if n % 2 == 0]
print a_list3comp

# filter and lambda way
a_list3lambda = filter(lambda n: n % 2 == 0, nums)
print a_list3lambda

# print letter number pair in "abcd" and "1234" (all possible pairs)
a_list4 = []
for letter in "abcd":
    for num in range(1,5):
        a_list4.append((letter,num))
print a_list4

a_list4comp = [(letter,num) for letter in "abcd" for num in range(1,5)]
print a_list4comp

# Dictionary comprehension
names = ["Bruce", "Clark", "Peter", "Logan", "David"]
heroes = ["Batman", "Superman", "Spiderman", "Wolverine", "Hulk"]
ages = [55, 200, 22, 1000, 40]
print zip(names, heroes, ages)
# creates touple matched by same index
a_dictionary = {}
for name, hero, age in zip(names, heroes, ages):
    a_dictionary[name] = hero
print "names heroes dictionary"
print a_dictionary

# age = ages.get("Bruce", "Unknown")
# print "Bruce is %s years old" % age

# list comprehension
a_dicComp = {name : hero for name, hero in zip(heroes, names)}
print "names heroes dictionary via list comp"
print a_dicComp

a_dicComp_age = {name : age for name, age in zip(names, ages)}
print "superhero ages"
print a_dicComp_age
# remove the shitty super hero
a_dicComp2 = {name : hero for name, hero in zip(names, heroes) if name != "Bruce"}
print a_dicComp2

# Set comprehension - like a list but has all unique values
# loop through and add values to set of unique values
nums2 = [1,2,3,1,3,2,5,6,7,5,4,9,9,8,7,7,7]
a_set = set()
for n in nums2:
    a_set.add(n)
print a_set

a_setComp = {n for n in nums2}
print a_setComp

# get not working for list
# third_num = nums2.get(index[2])
# print nums2
# print "third num is %n" % third_num

# Generator Expressions
# yield number * number for each number in nums
# def ntimesn(nums):
#     for n in nums:
#         yield n * n
# a_gen = ntimesn(nums)
# print a_gen

# generator is similar to list comprehension
a_gen2 = (n*n for n in nums)

for i in a_gen2:
    print i

myList = range(0,100)

# function that multiplies each number in myList by a given number
def ntimesit (parameter, myList):
    return [parameter * num for num in myList]
print ntimesit(2,myList)
print ntimesit(.5, myList)

# filter out values in myList by a parameter then multiply that filtered set by
# another parameter
def filterAndMultiply(alist, x, y):
    filterit = [num for num in alist if num > y]
    timesit = [x * num for num in filterit]
    return timesit

print filterAndMultiply(myList, 100, 20)

# function that return a probability given two parameters
def probabilityFunc(c,n):
    return (float(c)/n)*100

# then find the probability that if random number from myList \
# that it will be even using probabilityFunc
# function for even numbers
evenNumbers = [n for n in myList if n % 2 == 0]

totalEven = len(evenNumbers)
totalNumbers = len(myList)
probabilityEven = probabilityFunc(totalEven, totalNumbers)
print probabilityEven
print "probability of selecting even number,\
from a range of numbers 0 to 100 is {}%".format(probabilityEven)

# function for probability of list of numbers greater than a parameter
def cumulativeProbability(numsList, q):
    greaterThan = [num for num in numsList if num > q]
    totalGreater = len(greaterThan)
    probability = float(totalGreater)/len(numsList)
    return probability
print "percent of numbers greater than 20 in range of numbers 0 to 100 .\
is : {}".format(cumulativeProbability(myList, 20))

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
# prints lengths of words not including "the"
print word_lengths

names = ["Bruce", "Clark", "Peter", "Logan", "David"]
heroes = ["Batman", "Superman", "Spiderman", "Wolverine", "Hulk"]

# enumerate
for i, name in enumerate(names):
    print(i, name)

Xlist = [1,3,5,2,3]
Ylist = [9,6,8,5,7]
# zip
for x, y in zip(Xlist, Ylist):
     print (x, y)

x = 1
y = 9
# swap X and Y values
print "before x = %d, y= %d" % (x , y)
# touple unpacking
x, y = y, x
print "after x = %d, y = %d" % (x , y)

print "before Xs = {}, Ys = {}" .format(Xlist, Ylist)
Xlist, Ylist = Ylist, Xlist
print "after Xs = {}, Ys = {}" .format(Xlist, Ylist)

needle = "d"
haystack = ["a", "b", "c", "d"]
print "needle in haystack?"
for letter in haystack:
    if needle == letter:
        print "Found!"
        break
else:
    print "Not Found!"

# with open (file.txt) as f:
#     for line in f:
#         print (line)

try:
    print(int("x"))
except:
    print "Conversion Failed!"
else:
    print "Conversion Successful"
finally:
    print "Done"
