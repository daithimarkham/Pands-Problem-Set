# David Markham 2019-02-24
# Soultion to number 3
# Write a program that prints all numbers 1000 and 10,000,
# That are divisible by 6 but not 12. 

lower = 1000
higher = 10000

x = 6 
y = 12

for a in range (lower, higher):
  if (a%x == 0) and (a%y !=0):
    print (x)