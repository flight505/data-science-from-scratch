#!/usr/bin/env python3


from collections import defaultdict
from collections import Counter

doc = ('I trying to write a Python code that will allow me to take in text, and read it line by line. In each line, the words just go into the dictionary as a key and the numbers should be the assigned values, as a list. For example, the file will be composed of hundreds of lines that have the same format as this')
#doc = "doc.txt"
#with open(doc) as f:
words = doc.split()
word_counts = {}

for word in words:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1


print(type(words))
print(word_counts.keys())
print(word_counts.values())