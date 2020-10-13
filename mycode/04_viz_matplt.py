#!/usr/bin/env python3
 
##########################################################
# Copyright (c) Jesper Vang <jesper_vang@me.com>         #
# Created on 12 Oct 2020                                 #
# Version:	0.0.1                                        #
##########################################################

import os

from matplotlib import markers
from matplotlib.pyplot import plot
from matplotlib import pyplot as plt
from collections import Counter

os.system('cls||clear') # this line clears the screen 'cls' = windows 'clear' = unix

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

def plot_line(years,gdp): 
    """
    A basic line plot with matplotlib 
    """
    # create a line chart, years on x-axis, gdp on y-axis
    plt.plot(years, gdp, color='green', marker='o', linestyle='solid') # add a title
    plt.title("Nominal GDP")
    # add a label to the y-axis
    plt.ylabel("Billions of $") 
    return plt.show()

#plot_line(years,gdp)

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"] 
num_oscars = [5, 11, 3, 8, 10]

def plot(movies,num_oscars):
    """
    A basic bar plot with matplotlib 
    """
    # plot bars with left x-coordinates [0, 1, 2, 3, 4], heights [num_oscars]
    plt.bar(range(len(movies)), num_oscars) 
    plt.title("My Favorite Movies") # add a title
    plt.ylabel("# of Academy Awards") # label the y-axis # label x-axis with movie names at bar centers
    plt.xticks(range(len(movies)), movies) 
    return plt.show()

#plot(movies, num_oscars)




x_vals = [x for x in range(0,10,2)]
y_vals = [x for x in range(2,25,5)]
print((x_vals))
def test(x_vals,y_vals):
    """
    A basic line plot with matplotlib with random values - shape is mXn 5x5
    """

    plt.plot(y, x, color='green', marker='o', linestyle='solid')
    plt.title("Header :Test")
    plt.ylabel("random numbers") # add a label to the y-axis
    return plt.show()
#plot(x_vals,y_vals)


grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
# Bucket grades by decile, but put 100 in with the 90s
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades) 

def histograms(grades,histogram):
    """
    plotting histograms of bucketed numeric values
    """
    plt.bar([x + 5 for x in histogram.keys()], # Shift bars right by 5
        histogram.values(),                    # Give each bar its correct height
        10,                                    # Give each bar a width of 10
        edgecolor=(0, 0, 0))                   # Black edges for each bar

    plt.axis([-5, 105, 0, 5])                  # x-axis from -5 to 105, 
                                               # y-axis from 0 to 5

    plt.xticks([10 * i for i in range(11)])    # x-axis labels at 0, 10, ..., 100
    plt.xlabel("Decile") 
    plt.ylabel("# of Students") 
    plt.title("Distribution of Exam 1 Grades") 
    return plt.show()

histograms(grades,histogram)
    

mentions = [500, 520]
years = [2017, 2018]

def box_with_range(mentions,years):
    """
    When creating bar charts it is considered especially bad form for your 
    y-axis not to start at 0, since this is an easy way to mislead people.
    - plt.axes
    """
    
    plt.bar(years, mentions, 0.8)
    plt.xticks(years)
    plt.ylabel("# of times I heard someone say 'data science'")
    # if you don't do this, matplotlib will label the x-axis 0, 1 
    # and then add a +2.013e3 off in the corner (bad matplotlib!) 
    plt.ticklabel_format(useOffset=False)

    # misleading y-axis does not show from 0 to above 550
    plt.axis([2016.5, 2018.5, 0, 550]) 
    plt.title("Not So Huge Anymore") 
    return plt.show()
    
box_with_range(mentions,years)