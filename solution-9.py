# David Markham 2019-03-25
# Solution for problem number 9 

# Write a program that reads in a text file and outputs every second line. 
# The program should take the filename from an argument on the command line.

userinput = input("Please open text file: ")

with open('userinput',  'r') as f:
    for l in f:
        print(2)