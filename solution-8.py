# David Markham 2019-03-25
# Solution for problem number 8.

# Write a program that outputs today’s date and time in the format,
# ”Monday, January 10th 2019 at 1:15pm”.

# Start off with entering the function for importing date and time.
import datetime
# Then I entered the following statement to get today's date and time. 
now = datetime.datetime.today()

# I then done some research online to help me get python code for different date formats.
# I could not find help on Puthon to output st,nd, rd and th so I searched on Stackflow for help.
# I then used if, elif and else statements to output the answer. 

day_month = int(now.strftime("%d"))
if day_month in (1,2,3):
    day_suffix = 'st'
elif day_month in (2,22):
    day_suffix = 'nd'
elif day_month in (3,23):
    day_suffix = 'rd'
else:
    day_suffix = 'th' 
    
# I then entered print todays date and time.
# This will output whatever the user enters in the required date/time format required in the problem.
print(now.strftime("%A %B %d")+day_suffix,(now.today().strftime("%Y %H:%M %p")))




# Below are a list of the websites I used to help me solve problem number 8. 
# https://www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.php 
# https://docs.python.org/3/library/datetime.html?highlight=how%20import%20date 
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior 
# https://stackoverflow.com/questions/3644417/python-format-datetime-with-st-nd-rd-th-english-ordinal-suffix-like 