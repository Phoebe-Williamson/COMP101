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

#Q2
word = str(input("Enter a word: "))
corect_word =(word[:1]).capitalize()
corect_word =(word[-1:]).upper()
print(f"The converted word is: {corect_word}")

#Q3
sentence = input("Please enter the sentence: ")
if "(" not in sentence and ")" not in sentence:
    print("No text to remove.")
else:
    for i in sentence:
        if i == "(":
            new_sentence = sentence.split("(")
        elif i == ")":
            new_sentence = sentence.split(")")
    print(new_sentence)

#Q4
password = input("Please enter your password:")
password = password.strip()
if len(password) < 9:
    print("Your password is invalid!")
elif "123" in password or "abc" in password:
    print("Your password is invalid!")
else:
    print("Your password is valid!")
'''
#
movie_list = []
keep_going = True
while keep_going:
    movie_name = input("Please enter the movie name or end to print the list: ")
    if movie_name == 'end':
        keep_going = False
    else:
        movie_list.append(movie_name)

print()
print("Movies List:")
print("==============")
print(movie_list)
































