# David Markham 2019-03-25
# Solution for problem number 9 

# Write a program that reads in a text file and outputs every second line. 
# The program should take the filename from an argument on the command line.

f = open('mobydick.txt', 'r')

s = f.read()

print(s)
with open('mobydick.txt', 'r') as f:
    count = 0
    for line in f:
        count+=1
        if count % 2 == 0:
            print(line) 

f.close()




# https://stackoverflow.com/questions/30551945/how-do-i-get-python-to-read-only-every-other-line-from-a-file-that-contains-a-po