##
# A file for lab 4
# Date:(11/03/24)

#Q2: laws about drinking and driving
# under 18yr olds never drink and drive
# between 18 and 21 you can drive but not drink
# abouve 21 you can drive but not after drinking
age = float(input("Enter your age: "))
if age < 18:
    print("You may not drive or drink.")
elif 18 <= age < 21: #checking if between 18 and 21
    print("You may drive but not drink.")
else: # that they are over 21
    print("You may drive and drink, but never drive after drinking!")

#Q3: test scores
test_score = int(input("Enter a test score: "))
if test_score < 60:
    grade = "F"
if test_score < 70:
    grade = "D"
if test_score < 80:
    grade = "C"
if test_score < 90:
    grade = "B"
else:
    grade = "A"
print(grade)

#Q4
num1 = 95
num2 = 110
num3 = 150
output = ""
if num1 > num2 and num3 < num2:
    output += "A"
    if num1 + num2 < 100:
        output += "B"    
        output += "C"
elif num3 >= num1:
    if num1 + num2 <= 200:
        output += "D"
    else:
        output += "E"
    output += "F"
else:
    if num2 <= num1:
        output += "G"
    elif num3 < num2:
        output += "H"
    else:
        output += "I"
output += "J"
print(output)

#Q5
num1 = 75
num2 = 50
num3 = 25
output = ""
if num1 > num2 and num3 < num2:
    output += "A"
    if num1 + num2 < 100:
        output += "B"    
        output += "C"
elif num3 >= num1:
    if num1 + num2 <= 200:
        output += "D"
    else:
        output += "E"
    output += "F"
else:
    if num2 <= num1:
        output += "G"
    elif num3 < num2:
        output += "H"
    else:
        output += "I"
output += "J"
print(output)

#Q6
amount = int(input("Enter an amount: "))
if 50<= amount <=500 and amount % 10 ==0:
    fifties = amount // 50
    tens = (amount - fifties * 50)// 10
    print(f"Thank you. You will receive {fifties} bill(s) of 50 and" +
          f" {tens} bill(s) of 10.")
else:
    print("Invalid amount.")

#Q7: zpdiac checker (assuming the input is alawys valid)
day = int(input("Enter the day: "))
month = str(input("Enter the month: "))
if month.capitalize() == "December":
    if 1 <= day <= 21:
        print(f"{day} {month.capitalize()} is Sagittarius.")
    elif 22 <= day <= 31:
        print(f"{day} {month.capitalize()} is Capricorn.")
elif month.capitalize() == "January":
    if 1 <= day <= 19:
        print(f"{day} {month.capitalize()} is Capricorn.")
    elif 20 <= day <= 31:
        print(f"{day} {month.capitalize()} is Aquarius.")
elif month.capitalize() == "February":
    if 1 <= day <= 18:
        print(f"{day} {month.capitalize()} is Aquarius.")
    elif 19 <= day <= 29:
        print(f"{day} {month.capitalize()} is Pisces.")
elif month.capitalize() == "March":
    if 1 <= day <= 20:
        print(f"{day} {month.capitalize()} is Pisces.")
    elif 21 <= day <= 31:
        print(f"{day} {month.capitalize()} is Aries.")
elif month.capitalize() == "April":
    if 1 <= day <= 19:
        print(f"{day} {month.capitalize()} is Aries.")
    elif 20 <= day <= 30:
        print(f"{day} {month.capitalize()} is Taurus.")
elif month.capitalize() == "May":
    if 1 <= day <= 20:
        print(f"{day} {month.capitalize()} is Taurus.")
    elif 21 <= day <= 31:
        print(f"{day} {month.capitalize()} is Gemini.")
elif month.capitalize() == "June":
    if 1 <= day <= 20:
        print(f"{day} {month.capitalize()} is Gemini.")
    elif 21 <= day <= 30:
        print(f"{day} {month.capitalize()} is Cancer.")
elif month.capitalize() == "July":
    if 1 <= day <= 22:
        print(f"{day} {month.capitalize()} is Cancer.")
    elif 23 <= day <= 31:
        print(f"{day} {month.capitalize()} is Leo.")
elif month.capitalize() == "August":
    if 1 <= day <= 22:
        print(f"{day} {month.capitalize()} is Leo.")
    elif 23 <= day <= 31:
        print(f"{day} {month.capitalize()} is Virgo.")
elif month.capitalize() == "September":
    if 1 <= day <= 22:
        print(f"{day} {month.capitalize()} is Virgo.")
    elif 23 <= day <= 30:
        print(f"{day} {month.capitalize()} is Libra.")
elif month.capitalize() == "October":
    if 1 <= day <= 22:
        print(f"{day} {month.capitalize()} is Libra.")
    elif 23 <= day <= 31:
        print(f"{day} {month.capitalize()} is Scorpio.")
elif month.capitalize() == "November":
    if 1 <= day <= 21:
        print(f"{day} {month.capitalize()} is Scorpio.")
    elif 22 <= day <= 30:
        print(f"{day} {month.capitalize()} is Sagittarius.")

#Q8
wave_length = float(input("Enter the wavelength: "))
if wave_length < 1e-11:
    print("A wavelength of", wave_length ,"m corresponds to an Gamma wave.")
elif 1e-11 <= wave_length < 1e-8:
    print("A wavelength of", wave_length ,"m corresponds to an X-Ray wave.")
elif 1e-8 <= wave_length < 3.8*(1e-7):
    print("A wavelength of", wave_length ,"m corresponds to an Ultraviolet wave.")
elif 3.8*(1e-7) <= wave_length < 7.5*(1e-7):
    print("A wavelength of", wave_length ,"m corresponds to a Visible wave.")
elif 7.5*(1e-7) <= wave_length < 1e-3:
    print("A wavelength of", wave_length ,"m corresponds to an Infrared wave.")
elif 1e-3 <= wave_length < 1:
    print("A wavelength of", wave_length ,"m corresponds to a Microwave wave.")
else:
    print("A wavelength of", wave_length ,"m corresponds to a Radio wave.")

import math
#Q9
first_value = float(input("Enter the value of sin(\u03C0/2): "))
second_value = float(input("Enter the value of cos(\u03C0): "))
third_value = float(input("Enter the value of sin(\u03C0/6): "))

one = math.sin(math.pi/2)
two = math.cos(math.pi)
three = math.sin(math.pi/6)

if (math.isclose(one, first_value, abs_tol = 0.001)):
    print("First answer is correct.")
else:
    print("First answer is incorrect.")
if (math.isclose(two, second_value, abs_tol = 0.001)):
    print("Second answer is correct.")
else:
    print("Second answer is incorrect.")
if (math.isclose(three, third_value, abs_tol = 0.001)):
    print("Third answer is correct.")
else:
    print("Third answer is incorrect.")

#Q10
integer = int(input("Enter an integer number: "))

if integer > 10: # checking is number is greater than 10
    if integer > 50:
        print("Very Big")
    else:
        print("Big")
else:
    if integer < 5:
        print("Very Small")
    else:
        print("Small")

#Q11
current_cart_amount = float(input("Enter the current cart amount: "))
member = input("Are you a member? (yes/no): ")

if member == "yes":
    if current_cart_amount >= 500:
         discount_rate = 0.15
    elif 300 <= current_cart_amount < 500:
        discount_rate = 0.10
    elif 200 <= current_cart_amount < 300:
        discount_rate = 0.08
    elif 100 <= current_cart_amount <200:
        discount_rate = 0.04
    else:
        discount_rate = 0.02
else:
    if current_cart_amount >= 500:
         discount_rate = 0.08
    elif 300 <= current_cart_amount < 500:
        discount_rate = 0.04
    else:
        discount_rate = 0

final_amount = current_cart_amount - (current_cart_amount * discount_rate)
print(f"Discount rate: {int(discount_rate * 100)}%")
print(f"Final amount to be paid: ${round(final_amount, 2)}")

