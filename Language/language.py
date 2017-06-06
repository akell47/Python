"""
Examine Properties of individual books
    - book lenth
    - number of unique words
    - how attributes cluster by language or authorship

Project Gutenberg - oldest digital library of books with over 50,000 books
are in a public domain - can be downloaded and read for free

"""
"""
Count the number of times a unique word appears in a given string text
use Counter tool from collections module
"""

text = "This is a sentence. First words of sentences start with a capital letter and end with a period, question mark, or exclamation in the English language."

def count_words(text):
    """
    count the number of times each word occurs in text.
    Returns dictionary key = words and values = word count_words
    """
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

print (count_words(text))

"""
Periods and puncuations are counted as words along with mixed case words"
Can address mixed case words my making the string all lowercase.
Addressing punctuaction - specify all the punctuations to skip then loop over that container
and replace every occurrence of a punctuaction with an empty string
"""

def count_words2(text):
    """
    count the number of times each word occurs in text.
    Returns dictionary key = words and values = word count_words
    accounts for mixed case words and punctuaction
    """
    text = text.lower()
    skips = [".", ",", ":", ";", "?", "!", '""', "''" ]
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

print (count_words2(text))

"""
Python provides a counter tool from the Collections module"
"""
from collections import Counter
def count_words_faster(text):
    text = text.lower()
    skips = [".", ",", ":", ";", "?", "!", '""', "''" ]
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts

print (count_words_faster(text))

print (count_words2(text) == count_words_faster(text))

print (len(count_words2("This comprehension check is to check for comprehension.")))

print (count_words2(text) is count_words_faster(text))

"""
Reading in a Book
Character encoding = how a computer reads characters
UTF-8 dominant encoding
"""

def read_book(title_path):
    """
    Read a book and return it as a string
    """
    with open(title_path, "r", encoding="utf-8") as current_file:
        text = current_file.read()
        text.replace("\n", "").replace("\r","")
    return text

text_book = read_book("./Books/English/shakespeare/Romeo and Juliet.txt")

print ("Number of characters in Romeo and Juliet:",len(text_book))

# ind = text_book.find("What's in a name?")
# print (ind)
#
# sample_text = text_book[ind:ind + 1000]
# print (sample_text)

"""
Computing Word Frequency Statistics
how many unique words and frequency in a given book
"""



def word_stats(t):
    """return number of unique words and frequencies"""
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

word_counts = count_words_faster(text_book)
(num_unique, counts) = word_stats(word_counts)

print ("Number of words in Romeo and Juliet:",(num_unique))
print ("Number of unique words in Romeo and Juliet:", sum(counts))

# text_book_German = read_book("./Books/German/shakespeare/Romeo und Julia.txt")
# word_counts = count_words_faster(text_book_German)
# (num_unique, counts) = word_stats(word_counts)
#
# print ("Number of characters in Romeo und Julia:"),len(text_book_German)
# print ("Number of words in Romeo und Julia:",num_unique)
# print ("Number of unique words in Romeo und Julia:", sum(counts))

"""
Reading Multiple Files
"""
import os
book_dir = "./"
