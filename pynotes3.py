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
