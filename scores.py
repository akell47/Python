# take weighted average of dictionary keys
this section takes a weighted average of dictionaries with float key arrays
from random import randint
print "Random Number"
print(randint(0,100))

dictionary1 = {
    "name"       : "Dictionary1",
    "numbersetA" : [21.0, 66.0, 39.0],
    "numbersetB" : [13.0, 22.0, 60.0, 55.0],
    "numbersetC" : [22.0, 85.0]
}

dictionary2 = {
    "name"       : "Dictionary2",
    "numbersetA" : [23.0, 17.0, 49.0],
    "numbersetB" : [37.0, 92.0, 82.0, 53.0],
    "numbersetC" : [13.0, 43.0]
}

def average(numbers):
    total = float(sum(numbers))
    return total / len(numbers)

print "Dictionary 1 Set A average"
print average(dictionary1["numbersetA"])
print "Dictionary 2 Set A average"
print average(dictionary1["numbersetA"])

def get_weighted_average(dictionary):
    A = average(dictionary["numbersetA"])
    B = average(dictionary["numbersetB"])
    C = average(dictionary["numbersetC"])
    return 0.1 * A + 0.3 * B + 0.6

print "Average of Dictionary 1"
print get_weighted_average(dictionary1)
print "Average of Dictionary 2"
print get_weighted_average(dictionary2)

dictionaries = [dictionary1, dictionary2]

def get_whole_average(dictionaries):
    results = []
    for dictionary in dictionaries:
        x = get_weighted_average(dictionary)
        results.append(x)
    return average(results)

print "Average of Dictionaries 1 and 2 with weighted average"
print get_whole_average(dictionaries)
