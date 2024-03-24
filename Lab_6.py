##
# A file for lab 6
# date (20/03/24)
#
'''
#Q1
factor = int(input("Enter a factor: "))
maximum = int(input("Enter a maximum: "))

sums = 0 
for n range(1, maximum+1):
    if n % factor == 0:
        sums += n

print(f"The sum of the multiples of {factor} between 1 and {maximum} is equal to {sums}.")

#Q5
string = str(input("Enter the string: "))

first_letter = string[0]
second_letter = string[-1]
print(f"The first and last letters are {first_letter} and {second_letter}.")

#Q6
number_name_list = ['one', 'two', 'three', 'four', 'five', 'six', 
                    'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
number_with_digits = int(input("Enter the number: "))

if 1 <= number_with_digits <= 12:
    number_with_letters = number_name_list[number_with_digits - 1]

print(f"{number_with_digits} is written {number_with_letters}")

#Q7
Grades = []
keep_going = True
while keep_going:
    grade_input = input("Enter a grade (blank to exit): ")
    if grade_input == "":
        keep_going = False
    else:
        grade = int(grade_input)
        Grades.append(grade)
        
print(f"Grades: {Grades}.")
if len(Grades) > 0:
    smallest = min(Grades)
    biggest = max(Grades)
    length = len(Grades)
    average = round(sum(Grades)/length, 1)

    print(f"The minimum grade is {smallest}.")
    print(f"The maximum grade is {biggest}.")
    print(f"The average grade is {average}.")

#Q8
first_name = str(input("Enter your first name: "))
last_name = str(input("Enter your family name: "))
number = int(input("Enter a number between 100 and 999: "))

first_upi_digit = str(first_name[0])
if len(last_name) < 3:
    family_name = str(last_name)
    digits = str(number)
    upi = first_upi_digit + family_name + digits
    print(f"Your UPI is {upi}.")
else:
    family_name = str(last_name[:3])
    digits = str(number)
    upi = first_upi_digit + family_name + digits
    print(f"Your UPI is {upi}.")

#Q9

word = str(input("Enter a word: "))

consonants = 0
not_vowel = "bcdfghjklmnpqrstvwxyz"
length = len(word)

for i in word:
    if i.lower() in not_vowel:
        consonants +=1
        
print(f"{consonants} consonants.")
'''
#Q10
expression = input("Enter an expression: ")

parentheses = "()"
count = 0
open_brackets = 0

for i in expression:
    if i == "(":
        open_brackets += 1
    elif i == ")":
        if open_brackets == 0:
            print("Incorrect.")
            quit()
        open_brackets -= 1
        count += 1

if open_brackets != 0:
    print("Incorrect.")
else:   
    print("Correct.")
    pairs = count
    print(f"There are {pairs} pairs of parentheses.")

