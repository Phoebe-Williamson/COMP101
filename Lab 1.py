##
# A file in the first lab
# date (2/03/24)
#
'''
# print Hello World
print("Hello World")

#using the type function
print(type(4))  # type int
print(type(7.9))  # type float
print(type("Hello"))  #type string
print(type("50.0"))  #type string

# testing and  fixng name error (added value for age)
age = 12
print(age)

# testing and fixing type error (changed '+' to ',')
age = 12
name = "jess"
print(age, name)

# using 3 print statements
print("A wizard is never late, Frodo Baggins.")
print("Nor is he early.")
print("He arrives precisely when he means to!")

# classmates name and hobbie test
name = "Isabella"
hobby = "Ultimate frisbe"
print("My classmate is ", name)
print("Their favourite hobby is ", hobby)

# print out net_income
tax_rate = 0.30
gross_income = 5000

#add your calculation here
tax_rate = tax_rate*gross_income
net_income = gross_income-tax_rate
print(net_income)

# making a sentnce (Q21)
# variables given
first_name = "Meera"
last_name = "Patel"
age = "27"

#print statement
print(first_name, last_name, "is", age, "years old.")


#one ounce is  28.35 grams (Q22)
weight_in_ounces = 2.5
one_ounce_to_grams = 28.35
# round fuction rounds to 1dp with having round(..., 1)
weight_in_grams = round(weight_in_ounces*one_ounce_to_grams, 1) 
print(weight_in_ounces, "ounces is", weight_in_grams, "grams.")

#Q23:
#Calculate the potential energy of a spring
spring_constant = 100
displacement = 0.5
half = 1/2
potential_energy = half*spring_constant*(displacement**2)
print("The potential energy of the spring is",potential_energy)
'''
#Q24:get montly loan repayment
#M= L((i(1+i)n)/((1+i)n−1)) (equation)
#variables
loan_amount = 650000 # L in equation
annual_interest_rate = 5 /100 # anual intrest rate, need to chnage to monthly
loan_length_years = 20
months_per_year = 12
payments= 240
# maths
monthly_intrest_rate = annual_interest_rate/months_per_year

# top of fraction: (i*(1+i)**n)
top_of_fraction= (monthly_intrest_rate*((1 + monthly_intrest_rate))** payments)

#bottom of fraction: ((1+i)n−1)
bottom_of_fraction= (((1+ monthly_intrest_rate)** payments)- 1)

#dividing fraction
dividing= (top_of_fraction/ bottom_of_fraction)

#timing by L
monthly_payment = round(loan_amount * dividing)
#printing equation out
print(monthly_payment)
print("You will need to pay $", monthly_payment, "monthly.")
