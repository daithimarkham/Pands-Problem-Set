# David Markham 2019-03-20
# Solution for Problem 4
# Write a program that asks the user to input any positive integer, 
# And outputs the successive values of the calculation. 
# At each step calculate the next value by taking the current value,
# And if it is even divide it by two, if it is odd, multiply by three and add one. 
# Have the program end if the current value is one. 


# Ask the user to input a positive integer. 
n = int( input("Please input a positive integer "))
# If the user inputs anything other than a positive integer we type the following.
# Helps the user to put in the correct integer and quits the program.
if n <= 0:
    print("Unfortunately this is not an integer")
    quit()
# "Def Collatz" checks if the numbers are odd or even and performs those calculations.
def collatz(n):
# The loop is repeated until the number reaches 1.
    while n !=1:
# If the number is divisible by two print the answer. 
        if n % 2 == 0:
         n = n // 2
         print(n)
# If the result is not even, the answer is multiplied by three and one added on to it. 
        else:
            n = n * 3 + 1
        print(n) 

