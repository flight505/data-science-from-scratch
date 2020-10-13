#!/usr/bin/env python3
 
##########################################################
# Copyright (c) Jesper Vang <jesper_vang@me.com>         #
# Created on 11 Oct 2020                                 #
# Version:	0.0.1                                        #
##########################################################

import os
#os.system('cls||clear') # this line clears the screen 'cls' = windows 'clear' = unix

from typing import List # note capital L

xs =[3.4,4.5,5,6] 
def total(xs: List) -> float:
    return sum(xs)


new_total = total(xs)
print(new_total)
#total(xs: 'fife')

def maximum(xs: list) -> float:
    return max(xs) + min(xs)

sums = maximum(xs)
print(sums)