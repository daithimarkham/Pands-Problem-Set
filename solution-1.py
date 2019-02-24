# David Markham 2019-02-17
# Solution to problem number 1
# Write a program that asks the user to input any positive integer
# And outputs the sum of all numbers between one and that number.

i = int(input ("Please enter a positive integer: "))
# Asks the user to input a positive integer number 

if i <= 0: 
  print("Unfortunately this is not a positive integer")
# This will prevent the user from entering anything other than a positive integer.
 

start = 10

ans = 0

i = 1


while i <= start:
  ans = ans + i
  i = i + 1
# While 'i' is less than or equal to start we keep adding the all the numbers until we reach 10. This is called a compound statement. 
# Python recognises that while 'i' less than 10 it will keep adding (while loop) until it has reached 10, or certain statements are true.
print(ans)
# This will give the user the answer. 