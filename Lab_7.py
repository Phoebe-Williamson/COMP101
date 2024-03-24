##
# a file for lab 7
# Author: Phoebe Williamson
# Date(24/03/24)
'''
#Q1
first = str(input("Please enter the first 6 letter word: "))
second = str(input("Please enter the second 6 letter word: "))

first_part = str(first[:4])
last_part = str(second[-3:])
name = first_part + last_part

print(f"New Pokemon name: {name}")
'''
#Q2
word = str(input("Enter a word: "))
corect_word =(word[:1]).capitalize()
corect_word =(word[-1:]).upper()
print(f"The converted word is: {corect_word}")
