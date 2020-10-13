#!/usr/bin/env python3
 
##########################################################
# Copyright (c) Jesper Vang <jesper_vang@me.com>         #
# Created on 29 Sep 2020                                 #
# Version:	0.0.1                                        #
##########################################################

import os
from os import read
from typing import Text
os.system('cls||clear') # this line clears the screen 'cls' = windows 'clear' = unix


def looping(x):
    """
    loop de loop
    """
    for i in range(x): 
        print(i) # first line in "for i" block
        for j in range(x):
            print(j) # first line in "for j" block
            print(i + j) # first line in "for j" block
        print(i)
    print("done looping")

#looping(1)

def convert(miles):
    print('miles in km is: ')
    return miles * 1.6

a = convert(4)

print(a)

def funk(x, y):
    return x + y

c = funk(3, 5)
print(c)

new = 3

def full_name(first = "What's-his-name", last = "Something"):
    return first + " " + last


full_name("Joel", "Grus")
full_name("Joel")
full_name(last="Grus")
# "Joel Grus"
# "Joel Something"
# "What's-his-name Grus"
print(full_name())

x = [1,2,3,4,5,6,7,8,9]

a = x[:4]
b = x[4:]

c = a+b
print(c)
f,g = a,b
print(f,g)

tweet = {
"user" : "joelgrus",
"text" : "Data Science is Awesome",
"retweet_count" : 100,
"hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys = tweet.items()
print(tweet_keys)

texts = """Imagine that you’re trying to count the words in a document. An obvious approach is to create a dictionary in which the keys are words and the values are counts. As you check each word, you can increment its count if it’s already in the dictionary and add it to the dictionary if it’s not"""

document = texts.split(' ')

word_count = {}
for word in document:
    if word in word_count:
        word_count[word] += 1
        #print(word_count)
    else:
        word_count[word] = 1 

print(word_count)


#here is a while loop 
age = 0
while age < 31:
    print(f'i haven´t reached 31 i am only {age}')
    age += 1

squares = [x**2 for x in range(10) if x % 2 == 0 or 1]
print(squares)

class CountingClicker():
    """
    A class can/should have a docstring, just like a function
    """
    def __init__(self, count = 0):
        """
        constructor
        """
        self.count = count

    def __repr__(self) -> str:
        return f'CountingClicker(count={self.count})' 
    
    def click(self, num_times = 1):
        """
        Click the clicker some number of times
        """
        self.count += num_times
    def read(self):
        return self.count

    def reset(self):
        self.count = 0

clicker = CountingClicker()
assert clicker.read() == 0, "clicker should start with count 0"
clicker.click()
clicker.click()
assert clicker.read() == 2, "after two clicks, clicker should have count 2" 
print(clicker.read())
#clicker.reset()
#assert clicker.read() == 0, "after reset, clicker should be back to 0"

