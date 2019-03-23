# David Markham 2019-03-23
# Problem number 6 

# Write a program that takes a user input string and outputs every second word.
# Please enter a sentence: The quick brown fox jumps over the lazy dog. 
# Result: The brown jumps the dog.
# This sentence contains all the letters of the English alphabet, which is known as a pangram.  


# First you get the user to enter a sentence. 
sentence=(input("Please enter a sentence: "))
# Then split the sentence into splits by using a space.
# Then you take every  second word from it using the [::2] splice.
words = sentence.split(' ')
# Print every second word in the sentence that the user enters.
print(words[::2])

# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str


