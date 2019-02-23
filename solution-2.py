# David Markham 2019-02-23
# Solution to number 2
# Write a program that outputs whether or not today is a day that begins with the letter T.

import datetime 


if datetime.datetime.today().weekday() == 1:
    print("Yay! Today is a day that begins with the letter T")
 # This statement determines if the day begins with a letter T or not by importing the date and time.
 # Monday starts with 0, Tuesday with 1, and so on up until Sunday which is 6.
elif datetime.datetime.today().weekday() == 3:
    print("Yay! Today is a day that begins with the letter T")
# Allows you to check if another day also begins with the letter T and prints if true. Like an "if" statement, but allows you to do as many "if" statements as you wish.
else:
    print("Unfortunately today does not begin with the letter T")
# This prints not true if the above statements do not begin with the letter T.



