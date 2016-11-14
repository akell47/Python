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
print zip(names, heroes)
# creates touple matched by same index
a_dictionary = {}
for name, hero in zip(names,heroes):
    a_dictionary[name] = hero
print a_dictionary

# list comprehension
a_dicComp = {name : hero for name, hero in zip(heroes,names)}
print a_dicComp

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
#     print i
