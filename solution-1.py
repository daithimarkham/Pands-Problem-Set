# David Markham 2019-02-17
# Solution to problem number 1
# Write a program that asks the user to input any positive integer
# And outputs the sum of all numbers between one and that number.

# Asks the user to input a positive integer number 
i = int(input("Please enter a positive integer"))

# This will prevent the user from entering anything other than a positive integer.
if i <= 0: 
  print("Unfortunately this is not a positive integer")

total = 0 

while i > 0:
    total = total + i
    i = i - 1
# While 'i' is greater than 0 add the total and the current value of "i" and overwrite the current total. 
# This is called a compound statement using a while loop. 
# i = i -1: If the user inputs the positive integer of 10, the program subtracts one from the current value and so on, down to 0.

# Prints the answer. 
print(total)