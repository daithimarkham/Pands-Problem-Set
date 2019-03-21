# Pands-problem-set
# Data Analytics Problem Set 2019 - G.M.I.T.

# - Problem number 1

I was asked to get the user to input a positive integer of 10 and output the sum of all numbers between 0 and 10. 
First I wrote a simple statement to get the user to input a positive integer, int(input ("Please enter a positive integer: "))

Asks the user to input the positive integer number.

Then I wrote the following statement. 

if i <= 0:
  print("Unfortunately this is not a positive integer")

This will prevent the user from entering anything other than a positive integer.


I started the calculation with total 
 
  total = 0


I calculated the the sum by entering the following formula: 

 while i > 0:
    total = total + i
    i = i - 1

I used a compound statement here, using the while loop. While "i" was greater than 0, add the total plus "i".

The last line, i = i - 1. Whatever the user enters, subtract 1 and keep going until it reaches 0, adding all while looping.

Then I entered print(ans) which gave us the sum of 55 if the user enters the positive integer of ten. 


# - Problem number 2

This problem required me to write a program which outputs whether or not today begins with the letter "T". 

I started by importing the date and time by entering the following statement:

 if datetime.datetime.today().weekday() == 1:

    print("Yay! Today is a day that begins with the letter T")

Monday is 0, Tuesday is 1 and so on. 

I then entered an elif statement which helps us determine if there is more than one day which begins with the letter "T", such as Thursday. 

elif datetime.datetime.today().weekday() == 3:
    print("Yay! Today is a day that begins with the letter T")

To finish with I entered an else statement as follows to give me the answer: 

else:
    print("Unfortunately today does not begin with the letter T")


# - Problem number 3

In this problem I had to write a program that prints all the numbers between 1000 and 10,000 that are divisible by six but not by twelve. 

The program should start with 1002, 1014, 1026 etc and end up with 9990. 

I used the built in range function which generates arithmetic continuation from 1000 towards the final number I entered in the range which was 10,000.
This was for i in range (1000, 10000)

Next I came up with two maths formulas as follows which enabled me to do calculation: 

if i % 6 == 0 and i % 12!=0.
This stated for all the numbers in the range that could be divided by six but not by twelve. 

Finally I typed print(i), which gave all the numbers that could be divided by six in the range. 

