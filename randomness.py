import random

# print (random.choice(["H", "T"]))
#
# print (random.choice([0,1]))
#
# print (random.choice([1,2,3,4,5,6]))
#
# print (random.choice(range(1,7)))
#
# print (random.choice(random.choice([range(1,7), range(1,9), range(1,11)])))

# print (random.choice(range(0,10)))
#
# print (random.choice(list([1,2,3,4])))

print (sum(random.sample(range(10),10)))

# print (sum(random.choice(range(10),10)))

# print (random.sample_sum(range(10),10))

print (sum(random.choice(range(10)) for i in range(10)))

print (random.sample(range(10),10))
