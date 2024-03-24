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
# print out in alphabetical order
password = input("Please enter your password:")
password = password.strip()
if len(password) < 9:
    print("Your password is invalid!")
elif "123" in password or "abc" in password:
    print("Your password is invalid!")
else:
    print("Your password is valid!")

#Q5
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
#look at l1 or l2 ass code to see
'''
#q6
current_upis = ['cron777', 'emac263', 'gclo450',
                'jcoc100', 'jduj117', 'lmes754', 'mjac999']
current_passwords = ['SuiiiAlNassr23', 'PcqcNP2022', 'WhatElse06',
                     'HatOn4414', 'BlanQueTTe2006', 'GoatWC2022', 'thriLLer82']

print("Current list of UPIs:", current_upis)
print("Current list of passwords:", current_passwords)

keep_running = True
while keep_running:
    letter = input("Enter A to add a UPI/password pair or D to delete a pair: ")
    if letter.upper() == "A": #add upi
        new_upi = input("Enter a new UPI: ")
        if new_upi in current_upis:
            print(f"{new_upi} is already used!")
            new_upi = input("Enter a new UPI: ")
        else:
            current_upis.append(new_upi)
            new_password = input("Enter a new password: ")
            current_passwords.append(new_password)
    elif letter.upper() == "D": #delete upi
        upi_to_delete = input("Enter the UPI to be deleted: ")
        if upi_to_delete not in current_upis:
            print("UPI does not match!")
            upi_to_delete = input("Enter the UPI to be deleted: ")
        else:
            #find upis key, find that key in passwords, set that to password
            #check if the password_entered is equal to password,
            #if not, say it does not match and ask again
            # if password matches, remove upi an dpassowrd from the lists

#Q7 need to add to list, reverse lost and then print out with comma between 
#and make sure there a no repetitions
sentence = input("Please enter a sentence: ")




























