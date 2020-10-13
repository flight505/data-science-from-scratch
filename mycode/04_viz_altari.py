
 
##########################################################
# Copyright (c) Jesper Vang <jesper_vang@me.com>         #
# Created on 12 Oct 2020                                 #
# Version:	0.0.1                                        #
##########################################################

import os
#os.system('cls||clear') # this line clears the screen 'cls' = windows 'clear' = unix


import altair as alt
from altair.vegalite.v4.api import Chart
from matplotlib.pyplot import title
import pandas as pd
import altair_viewer

data = pd.DataFrame({'x': ['A', 'B', 'C', 'D', 'E'],
                     'y': [5, 3, 6, 7, 2]})

def test_bar(data):
    """
    A test bar chart 
    """
    Chart = alt.Chart(data).mark_bar().encode(
        x='x',
        y='y',
    ).interactive()
    return altair_viewer.show(Chart)
# test_bar(data)

#-----------------------------------------------------
# Example from the book 
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"] 
num_oscars = [5, 11, 3, 8, 10]

# convert to a dataframe
data2 = pd.DataFrame({'movies' : ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"],
                      'num_oscars' : [5, 11, 3, 8, 10]})

def basic_bar(data2):
    """
    for a basic chart, convert data to a dataframe or other accepted data sources
    """
    Chart2 = alt.Chart(data2).mark_bar().encode(
        x='movies',
        y='num_oscars',
        color='movies',
    ).interactive()
    return altair_viewer.show(Chart2)
# basic_bar(data2)
                   


# with title and size
def bar_chart(data2):
    """
    A bar chart, like the one above but with small custom alterations title and size
    """
    
    Chart2 = alt.Chart(data2).mark_bar().encode(
        alt.X ('movies', title="My Favorite Movies"),
        alt.Y ('num_oscars', title="# of Academy Awards"),
        color='movies',
    ).properties(width=200).interactive()
    return altair_viewer.show(Chart2)
# bar_chart(data2)



data3 = pd.DataFrame({'variance' : [1, 2, 4, 8, 16, 32, 64, 128, 256],
                      'bias_squared' : [256, 128, 64, 32, 16, 8, 4, 2, 1]})
#total_error = [x + y for x, y in data3]

sum = pd.DataFrame(data3['variance'] + data3['bias_squared']) # a Series
print(sum)

xs = [i for i, _ in enumerate(variance)]


def bias_line_chart(data3):
    """
    docstring
    """
    Chart3 = alt.Chart(data3).mark_line().encode(
    x='variance',
    y='bias_squared'
    ).interactive()
    return altair_viewer.show(Chart3)

bias_line_chart(data3)


# Chart2 = alt.Chart(data).mark_bar().encode(
#     alt.X ('movies', title="My Favorite Movies"),
#     alt.Y ('num_oscars', title="# of Academy Awards"),
#     color='movies',
# ).properties(width=200).interactive()
# altair_viewer.show(Chart2)

# total_error = [x + y for x, y in zip(variance, bias_squared)] 
# xs = [i for i, _ in enumerate(variance)]
# # We can make multiple calls to plt.plot
# # to show multiple series on the same chart
# plt.plot(xs, variance, 'g-', label='variance') # green solid line 
# plt.plot(xs, bias_squared, 'r-.', label='bias^2') # red dot-dashed line 
# plt.plot(xs, total_error, 'b:', label='total error') # blue dotted line
# # Because we've assigned labels to each series,
# # we can get a legend for free (loc=9 means "top center") plt.legend(loc=9)
# plt.xlabel("model complexity")
# plt.xticks([])