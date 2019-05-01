
#Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically?

words=[x for x in input("enter the words :").split(',')]# list comprehension
words.sort()
print(','.join(words))