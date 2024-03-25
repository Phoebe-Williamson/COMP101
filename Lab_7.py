##
# a file for lab 7
# Author: Phoebe Williamson
# Date(25/03/24)
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
if len(word) == 1:
    correct_word = word.upper()
else:
    correct_word = (word[0:1].upper() + word[1:len(word)-1].lower() + word[len(word)-1:len(word)].upper())
print(f"The converted word is: {correct_word}.")

#Q3
sentence = input("Please enter the sentence: ")
if "("  in sentence and ")"  in sentence:
    end_delete = sentence.rfind(")")
    start_delete = sentence.find("(")
    new_sentence = (sentence[:(start_delete -1)] + sentence[end_delete +1:])
    print("New sentence after removal:", new_sentence)
else:
    print("No text to remove.")

#Q4
# print out in alphabetical order
number_count = 0
alphabet_count = 0

password = input("Please enter your password: ")
password = password.strip()

for i in password:
    if i.isalpha() == True:
        alphabet_count += 1
    elif i.isdigit() == True:
        number_count += 1

if len(password) < 9:
    print("Your password is invalid!")
elif "123" in password or "abc" in password:
    print("Your password is invalid!")
elif number_count < 5:
    print("Your password is invalid!")
elif alphabet_count < 4:
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
movie_list = list(set(movie_list))
movie_list.sort()
print()
print("Movies List:")
print("==============")
for movie_name in movie_list:
    movie_key = movie_list.index(movie_name)
    key = movie_key + 1
    print(f"{key}) {movie_name}")


#q6
current_upis = ['cron777', 'emac263', 'gclo450',
                'jcoc100', 'jduj117', 'lmes754', 'mjac999']
current_passwords = ['SuiiiAlNassr23', 'PcqcNP2022', 'WhatElse06',
                     'HatOn4414', 'BlanQueTTe2006', 'GoatWC2022', 'thriLLer82']

print("Current list of UPIs:", current_upis)
print("Current list of passwords:", current_passwords)

letter = input("Enter A to add a UPI/password pair or D to delete a pair: ")
keep_running = True
while keep_running:
    if letter.upper() == "A": #add upi
        new_upi = input("Enter a new UPI: ")
        if new_upi in current_upis:
            print(f"{new_upi} is already used!")
        else:
            current_upis.append(new_upi)
            new_password = input("Enter a new password: ")
            current_passwords.append(new_password)
            print("Updated list of UPIs:", current_upis)
            print("Updated list of passwords:", current_passwords)
            break

    elif letter.upper() == "D": #delete upi
        upi_to_delete = input("Enter the UPI to be deleted: ")
        if upi_to_delete not in current_upis:
            print(f"{upi_to_delete} does not exist!")
        else:
            password = input("Enter the current password: ")
            password_key = current_upis.index(upi_to_delete)
            verify_password = current_passwords[password_key]
            if password != verify_password:
                print("The password does not match!")
            else:
                current_upis.pop(password_key)
                current_passwords.pop(password_key)
                print("Updated list of UPIs:", current_upis)
                print("Updated list of passwords:", current_passwords)
                break
                

'''
#Q7 need to add to list, reverse lost and then print out with comma between 
#and make sure there a no repetitions
sentence = input("Please enter a sentence: ")



























