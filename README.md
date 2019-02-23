# pands-problem-set
Data Analytics Problem Set 2019 - G.M.I.T.

Problem 1

In this problem we were asked to get the user to input an integer and output the sum of all numbers between zero and ten. 

First we write a simple statement to get the user to input the integer 10, int(input ("Please enter an integer: 10"))

Asks the user to input the positive integer number 10.

We started the calculation with three simple elements.

  start = 10

  ans = 0 

  i = 1

We then wrote the following to help the user get the desired sum at the end of the calculation. 

if ans> 10: 
  print("Unfortunately this is not a positive integer")

We calculated the the sum by entering the following formula: 

  while i <= start:

    ans = ans + i

    i = i + 1