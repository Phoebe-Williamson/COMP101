##
# A file for lab 3
'''
#Q2
result = 2 * 7 // 3 - 5 // 3 + 3 % 2 
print("Result:", result)

#Q3
result1 = 22 % 5 + 33 % 6
result2 = 33 % 3 + 6 % 12 - 15 % 15
print(f"result1: {result1} result2: {result2}")

#Q4
weather = input("Enter the current weather: ")
if weather == "Sunny":
    print("Barbecue time!")
if weather != "Sunny":
    print("Better avoid barbecue.")
    print("Try again tomorrow.")
print("Powered by BarbecuePredictor.co.nz")

#Q5
weather = input("Enter the current weather: ")
if weather == "Sunny":
    print("Barbecue time!")
else:
    print("Better avoid barbecue.")
    print("Try again tomorrow.")

#Q6
weather = input("Enter the current weather: ")
if weather == "Sunny":
    print("Barbecue time!")
    weather = "Unknown" 
elif weather == "Unknown": 
    print("Your choice.") 
elif weather != "Sunny":
    print("Better avoid barbecue.")
    print("Try again tomorrow.")
else:
    print("Powered by BarbecuePredictor.co.nz")

#Q7
password = input("Kia ora. Enter your password: ")
verify_password = input("Verify your password: ")
if verify_password == password:
    print("Passwords match")
else:
    print("Passwords do not match")
print("Ngā mihi.")

#Q8
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
# if they are equal
if first_number == second_number:
    print(f"{first_number} equal to {second_number}: True")
else:
    print(f"{first_number} equal to {second_number}: False")
# if num1 is greater than num2
if first_number > second_number:
    print(f"{first_number} greater than {second_number}: True")
else:
    print(f"{first_number} greater than {second_number}: False")
#if num1 is less than num2
if first_number < second_number:
    print(f"{first_number} less than {second_number}: True")
else:
    print(f"{first_number} less than {second_number}: False")
#if num1 is not equal to num2
if first_number != second_number:
    print(f"{first_number} not equal to {second_number}: True")
else:
    print(f"{first_number} not equal to {second_number}: False")
#if num1 is greater than or equal to num 2
if first_number >= second_number:
    print(f"{first_number} greater than or equal to {second_number}: True")
else:
    print(f"{first_number} greater than or equal to {second_number}: False")
#if num1 is less than or equal to num 2
if first_number <= second_number:
    print(f"{first_number} less than or equal to {second_number}: True")
else:
    print(f"{first_number} less than or equal to {second_number}: False")

#Q9
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))
if denominator == 0:
    print("Result: Undefined")
else:
    equation = round(numerator/denominator, 2)
    print(f"Result: {equation}")

#Q10
import math
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
sum = first_number + second_number
square = math.sqrt(first_number + second_number)
if round(square) == square:
    print(f"The sum of {first_number} and {second_number} is a square number.")
else:
    print(f"The sum of {first_number} and {second_number}" +
          " is not a square number.")

#Q11
month_list_1 = ["February"]
month_list_2 = ["January", "March", "May", "July", "August", "October", "December"]
month_list_3 = ["April", "June", "September", "Novemeber"]
month = str(input("Enter the name of a month: "))
if month.capitalize() in month_list_1:
    print(month.capitalize(), "has 28 days.")
elif month.capitalize() in month_list_2:
    print(month.capitalize(), "has 31 days.")
else:
    print(month.capitalize(), "has 30 days.")

#Q12
year = int(input("Enter a year: "))
if year % 12 == 2000 % 12:
    print(year, "is the year of the Dragon.")
elif year % 12 == 2001 % 12:
    print(year, "is the year of the Snake.")
elif year % 12 == 2002 % 12:
    print(year, "is the year of the Horse.")
elif year % 12 == 2003 % 12:
    print(year, "is the year of the Sheep.")
elif year % 12 == 2004 % 12:
    print(year, "is the year of the Monkey.")
elif year % 12 == 2005 % 12:
    print(year, "is the year of the Rooster.")
elif year % 12 == 2006 % 12:
    print(year, "is the year of the Dog.")
elif year % 12 == 2007 % 12:
    print(year, "is the year of the Pig.")
elif year % 12 == 2008 % 12:
    print(year, "is the year of the Rat.")
elif year % 12 == 2009 % 12:
    print(year, "is the year of the Ox.")
elif year % 12 == 2010 % 12:
    print(year, "is the year of the Tiger.")
elif year % 12 == 2011 % 12:
    print(year, "is the year of the Hare.")
'''
#Q13
print("A quadratic equation has the form: ax^2 + bx + c")
a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
c = int(input("Enter the value for c: "))



    
