import string
alphabet = string.ascii_letters


sentence = 'Jim quickly realized that the beautiful gowns are expensive'
# dictionary of letters and iterate through
# count_letters = {}


def counter(input_string):
    count_letters = {}
    for letter in sentence:
        if letter in alphabet:
            if letter in count_letters:
                count_letters[letter] += 1
            else:
                count_letters[letter] = 1
    return count_letters

# address_count = counter(address)
# print (address_count)
sen_count = counter(sentence)
print (sen_count)
print "----"
most_fequent_letter = max(sen_count, key=sen_count.get)
