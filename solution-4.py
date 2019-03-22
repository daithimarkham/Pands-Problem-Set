# David Markham 2019-03-20
# Solution for Problem 4
# Write a program that asks the user to input any positive integer, 
# And outputs the successive values of the calculation. 
# At each step calculate the next value by taking the current value,
# And if it is even divide it by two, if it is odd, multiply by three and add one. 
# Have the program end if the current value is one. 


# Ask the user to input a positive integer. 
n = int(input("Please input a positive integer: "))
# "Def Collatz" checks if the numbers are odd or even and performs those calculations.
def collatz(n):

# The loop is repeated until the number reaches 1.
    while n > 1:
# This function prints all the values listed from the number the user enters to the end.
        print(n, end =' ') 
        if (n % 2): 
# If the result is not even, the answer is multiplied by three and one added on to it. 
            n = 3 * n + 1
#If the number is even divide by two until you reach the number one. 
        else:
            n = n//2
    print(1, end='')

# This will print the sequence of the calculation, down as far as the end number such as one.
print("Sequence: ", end='')
collatz(n) 



