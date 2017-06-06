import string

# alphabet = lowercase letters,  with a space.
alphabet = string.ascii_lowercase + " "
numbers = list(range(0,27))
print (alphabet)
print (numbers)

# dictionary with number as keys from 0 to 26 with the space, and alphabet
# letters = { number: letter for number, letter in zip(numbers, alphabet) }
# print (letters)

letters = dict(enumerate(alphabet))
print (letters)

encryption_key = 3
encoding = {letter: (place + encryption_key) % 27 for place, letter in enumerate(alphabet)}
print (encoding)

message = "hi my name is caesar"


def caesar(message, encryption_key):
    """
    This is a Caesar cipher.  Each letter in a message is shifted by a few
    characters in the alphabet, and returned.

    message:        A string you would like to encode or decode.  Must consist of
                    lowercase letters and spaces.
    encryption_key: An integer, indicating how many characters each letter in the
                    message will be shifted.
    """
    encoding = {letter: (place + encryption_key) % 27 for (place, letter) in enumerate(alphabet)}
    coded_message = "".join([letters[encoding[letter]] for letter in message])
    return coded_message

encoded_message = caesar(message, encryption_key=3)
print(encoded_message)

decoded_message = caesar(encoded_message, encryption_key=-3)
print (decoded_message )
