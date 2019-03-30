# David Markham 2019-03-26
# Solution for problem number 10

# Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].

# First import the built-in matplotlib and Numpy functions which generate data.
# This will plot the functions listed on a graph. 
# # https://realpython.com/python-matplotlib-guide/ found info here.
import matplotlib.pyplot as pl 
import numpy as np 

# This will provide the data for the x-axis. 
x = np.arange (0.0, 4.0, 0.5)

# This will list the functions.
y1 = x 
y2 = x**2
y3 = 2**x

# This plots the functions within the range listed in the problem.
# Found info on this site which helped me for this part. 
# # https://realpython.com/python-matplotlib-guide/ 
pl.plot([0,4])
# This will provide a sequence of values for the x and y lists on the graph.
pl.xlabel('X-Axis')
pl.ylabel('Y-Axis')


# This displays the graph with the functions on the X and Y axis for the user.
pl.show() 

