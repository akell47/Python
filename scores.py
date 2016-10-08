lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# numbers = ([5,6,10])
def average(numbers):
    total = float(sum(numbers))
    return total / len(numbers)

# print average(numbers)
print "Lloyd test average:"
print average(lloyd["tests"])
print "Alice test average:"
print average(alice["tests"])
print "Tyler test average:"
print average(tyler["tests"])

def get_average(student0A):
    homework = average(student0A["homework"])
    quizzes = average(student0A["quizzes"])
    tests = average(student0A["tests"])
    return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

print "Lloyd class average"
print get_average(lloyd)
print "Alice class average"
print get_average(alice)
print "Tyler class average"
print get_average(tyler)

def get_letter_grade(score):
    if score >= 90.0:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print "Lloyd letter grade"
print get_letter_grade(get_average(lloyd))
print "Alice letter grade"
print get_letter_grade(get_average(alice))
print "Tyler letter grade"
print get_letter_grade(get_average(tyler))

students = ["lloyd","alice","tyler"]

def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
        print results
    return average(results)

print results


# def get_class_letter(students0C)
