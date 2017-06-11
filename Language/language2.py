"""
Reading in a Book
Character encoding = how a computer reads characters
UTF-8 dominant encoding
"""
from io import open
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

from collections import Counter
def count_words_faster(text):
    text = text.lower()
    skips = [".", ",", ":", ";", "?", "!", '""', "'", '\n', "-", "(", ")", "[", "]"]
    for ch in skips:
        text = text.replace(ch, "")
        word_counts = Counter(text.split(" "))
    return word_counts

print len(count_words_faster(text_book))

def word_stats(word_counts):
    """return number of unique words and frequencies"""
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

word_counts = count_words_faster(text_book)
(num_unique, counts) = word_stats(word_counts)

print ("Number of words in Romeo and Juliet:",(num_unique))
print ("Number of unique words in Romeo and Juliet:", sum(counts))


def word_count_distribution(text):
    dict_words = (count_words_faster(text))
    print "dict_words",dict_words
    distribution = dict(Counter(dict_words.values()))
    print "distribution",distribution
    return distribution

"""text book"""
distribution = word_count_distribution(text_book)

import numpy as np
def more_frequent(distribution):
    counts = list(distribution.keys())
    frequency_of_counts = list(distribution.values())
    print "counts", (counts)
    print "frequency",(frequency_of_counts)
    cumulative = np.cumsum(frequency_of_counts)
    print "cumulative",cumulative
    more_frequent = (1.0 - cumulative) / cumulative[-1]
    print "more frequent",more_frequent
    return dict(zip(counts, more_frequent))

print more_frequent(distribution)
