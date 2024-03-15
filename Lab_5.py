##
# A file for lab 5
# Date (14/3/24)
# Author: Phoebe Williamson, 117889335
#
'''
#Q1: checking what kind of triangle
first_side = int(input("Enter the length of the first side: "))
second_side = int(input("Enter the length of the second side: "))
third_side = int(input("Enter the length of the third side: "))

condition_1 = first_side >= second_side + third_side
conditon_2 = second_side >= third_side + first_side
condition_3 = third_side >= first_side + second_side

if condition_1 or conditon_2 or condition_3: # no triangle
    print("The triangle does not exist.")
elif first_side == second_side and first_side == third_side : # equilateral
    print("The triangle is equilateral.")
elif first_side == second_side or first_side == third_side or third_side == second_side: # isosceles
    print("The triangle is isosceles.")
else: # obtuse
    print("The triangle is obtuse.")

#Q2 ask user for two numbers and an opperator, all numbers to be orunded to 2dp
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operator = input("Enter the operator: ")

# checks if opperator is valid
if operator != "+" and operator != "-" and operator != "*" and operator != "/":
    print("Operator not supported.")
elif operator == "+": # addition
    round_1 = round(first_number, 1)
    round_2 = round(second_number ,1)
    result = round(round_1 + round_2, 1)
    print(f"{round_1} + {round_2} = {result}")
elif operator == "-": # subtraction
    round_1 = round(first_number, 1)
    round_2 = round(second_number ,1)
    result = round(round_1 - round_2, 1)
    print(f"{round_1} - {round_2} = {result}")
elif operator == "*": #multiplication
    round_1 = round(first_number, 1)
    round_2 = round(second_number ,1)
    result = round(round_1 * round_2, 1)
    print(f"{round_1} * {round_2} = {result}")
else:
    round_1 = round(first_number, 1)
    round_2 = round(second_number ,1)
    result = round(round_1 / round_2, 1)
    print(f"{round_1} / {round_2} = {result}")

#Q4 asks user for pos integer, then prints numbers between 0 and pos integer
pos_int = int(input("Enter a positive integer: "))
total = 0
while total <= pos_int:
    print(total, end=" ")
    total += 1

#Q5
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

smallest = min(number_1, number_2)
biggest = max(number_1, number_2)

number = smallest
while number <= biggest:
    print(number, end=" ")
    number += 1

#Q6
amount = int(input("Enter an amount, multiple of 10: "))
while amount %10 != 0 :
    amount = int(input("Enter an amount, multiple of 10: "))

print(f"Thank you. You will receive NZD{amount} in bill(s) of 10.")

#Q7
factor = 2
number = int(input("Enter a number: ")) # asks user for number
if number < 2: # checks if number is less than 2
    print("No prime factors")
else:
    print(f"The prime factors of {number} are:") # prints out the prime facotrs
    while factor <= number:
        if number % factor == 0:
            print(factor)
            number = number // factor
        else:
            factor += 1

#Q8
one_cny_to_nzd = 0.22
amount = round(float(input("Enter an amount in NZD: ")), 1)
cny_amount = round(amount / one_cny_to_nzd, 2)
print(f"{amount} NZD is equivalent to {cny_amount} CNY")
keep_going = True
while keep_going:
    again = str(input("Convert another amount (y/n)? "))
    if again == "n":
        keep_going = False
    else:
        amount = round(float(input("Enter an amount in NZD: ")), 1)
        cny_amount = round(amount / one_cny_to_nzd, 2)
        print(f"{amount} NZD is equivalent to {cny_amount} CNY")
'''
#Q9
invalid = 0
start = int(input("Enter the range start: "))
end = int(input("Enter the range end: "))
between = int(input(f"Enter an integer between {start} and {end} (inclusive): "))

keep_going = True
while keep_going:
    if between < start or between > end:
        invalid += between
        between = int(input(f"Enter an integer between {start} and {end} (inclusive): "))
    else:
        keep_going = False
print(f"The total of all the invalid integers is {invalid}.")
