#!/usr/bin/env python3
 
##########################################################
# encoding: utf                                          #
# Copyright (c) Jesper Vang <jesper_vang@me.com>         #
# MIT Licence. See http://opensource.org/licenses/MIT    #
# Created on 26 Jul 2020                                 #
# Version:	0.0.1                                        #
##########################################################

def double(x):
    """This is where you put an optional docstring that explains what the function does. For example, this function multiplies its input by 2. """
    return x*2

out = double(3)
print(f'{out}')

def apply_to_one(f):
    """Calls the function f with 1 as its argument""" 
    return f(1)


my_double = double # refers to the previously defined function 
x = apply_to_one(my_double) # equals 2   


def my_print(message="world"):
    print(message)


my_print("hello") # prints 'hello'
my_print() # prints 'my default message'

tab_string = "the word" # represents the tab character 
count = len(tab_string) # is 1
