# David Markham 2019-03-25
# Solution for problem number 9 

# Write a program that reads in a text file and outputs every second line. 
# The program should take the filename from an argument on the command line.

# This is extra pieces of information that the user provided to your Python script.
# Foe eg, what the text file is called that the user wants to use.
import sys
# Write a statement to get the user to enter the file they wish to use. 
user = input("Please enter file name: ")

# I was having trouble finding the help on the Python tutorial so I went to Stack Overflow for help;
# https://stackoverflow.com/questions/30551945/how-do-i-get-python-to-read-only-every-other-line-from-a-file-that-contains-a-po
# This prints every even line, which is the equivalent of every second line of the user input. 
# I created a text file: mobydick.txt to ensure it was correct which it was. 
with open(user, 'r') as f:
    count = 0
    for line in f:
        count+=1
        if count % 2 == 0:
            print(line) 
# f.close() is good practice to end the program when you've finished. 
f.close()





# 