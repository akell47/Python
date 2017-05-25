import string

# alphabet = lowercase letters,  with a space.
alphabet = string.ascii_lowercase + " "
numbers = list(range(0,27))
print (alphabet)
print (numbers)

# dictionary with number as keys from 0 to 26 with the space, and alphabet
letters = { number: letter for number, letter in zip(numbers, alphabet) }
print (letters)
