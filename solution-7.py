# David Markham 2019-03-23
# Problem number 7 

# Write a program that that takes a positive floating point number as input
# And outputs an approximation of its square root.


# This is the built in function to calculate the square root in Python.
import math 
# This asks the user to input a positive floating point number. 
n = float(input("Please enter a positive floating point number: "))
# This will ensure the user puts in a positive floating point number.
while n <= 0:
    print("Unfortunately this is not a positive floating integer")
    
# This is the floating point computation to get the square root of the user input.
n_sqrt = n ** 0.5
# This will print the square root, with one floating point. (%.1f) 
print('The square root of %0.1f is %0.1f'%(n ,n_sqrt))


# Ref; viewed on 2019-03-24,  https://www.programiz.com/python-programming/examples/square-root