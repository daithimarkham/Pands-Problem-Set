# David Markham 2019-02-17
# Solution to problem number 1
# Write a program that asks the user to input any positive integer
# And outputs the sum of all numbers between one and that number.

int(input ("Please enter a positive integer: "))
# Asks the user to input a positive integer number.

start = 10
# 10 is the number that is the end of the calculation.
ans = 0 
# ans is where the answer started and what it would finally become, 1+2+3+4 and so on, up until number 10.
i = 1
# keeps track of where you are in the calculation 

if ans> 10: 
  print("Unfortunately this is not a positive integer")
# This will help the user get the desired sum. Anything greater than 10, or less than zero is an invlaid integer. 

while i <= start:
    ans = ans + i
    i = i + 1
# While 'i' is less than or equal to start we keep adding the all the numbers until we reach 10. This is called a compound statement. 
# Python recognises that while 'i' less than 10 it will keep adding (while loop) until it has reached 10, or certain statements are true.
print(ans)
# This will give the user the answer. 