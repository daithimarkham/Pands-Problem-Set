# David Markham 2019-03-22
# Solution to Problem number 5

# Write a program that asks the user to input a positive integer,
# And tells the user whether or not the number is a prime.
# A prime number is an integer which has only two factors, one and itself. 
# Numbers which have more than two factors are composite numbers. 



# Asks the user to input a positive integer.
n = int(input("Please enter a positive integer: "))
# This will help the user to input a positive integer.
if n < 1:
    print("Unfortunately this is not a positive integer")



# I was having difficulty in solving this problem so I found a source online which helped me solve it. 
# Please find link below. 
# https://www.programiz.com/python-programming/examples/prime-number 

if n > 1:
# This checks for the factors, does the modulus give you a remainder when divided by the input. 
# And states whether or not it is a prime number when it does the calculation. 
# This is achieved by if and else statements.
   for i in range(2,n):
       if (n % i) == 0:
# This will state if the number is composite number, which has factors other than one and itself.
           print(n,"is not a prime number")
           break
   else:
       print(n,"is a prime number")
       
 

            