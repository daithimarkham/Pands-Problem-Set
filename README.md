# Pands-problem-set
# Data Analytics Problem Set 2019 - G.M.I.T.

# - Problem number 1

I was asked to get the user to input a positive integer and output the sum of all numbers between 0 and 10. 

First I wrote a simple statement to get the user to input the integer 10, int(input ("Please enter a positive integer: 10 "))

Asks the user to input the positive integer number.

I started the calculation with three simple elements.

  start = 10

  ans = 0 

  i = 1

I then wrote the following to help the user get the desired sum at the end of the calculation. 

if ans> 10: 
  print("Unfortunately this is not a positive integer")

I calculated the the sum by entering the following formula: 

  while i <= start:

    ans = ans + i

    i = i + 1

Then I entered print(ans) which gave us the sum of 55. 


# - Problem number 2

This asked us to write a program which outputs whether or not today begins with the letter "T". 

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


