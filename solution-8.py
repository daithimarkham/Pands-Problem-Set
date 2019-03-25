# David Markham 2019-03-25
# Solution for problem number 8.

# Write a program that outputs today’s date and time in the format,
# ”Monday, January 10th 2019 at 1:15pm”.

# Start off with entering the function for importing date and time.
import datetime
# Then I entered the following statement to get today's date and time. 
now = datetime.datetime.now() 
# I then done some research online to help me get python code for different date formats.
# I then entered print todays date and time.
# This will output whatever the user enters in the required date/time format required in the problem.
print (now.strftime("%A %dth %B %Y %H:%Mpm"))




# https://www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.php 
# https://docs.python.org/3/library/datetime.html?highlight=how%20import%20date 