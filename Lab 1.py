##
# A file in the first lab
# date (29/02/24)
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
'''

#one ounce is  28.35 grams (Q22)
weight_in_ounces = 2.5
one_ounce_to_grams = 28.35
weight_in_grams = round(weight_in_ounces*one_ounce_to_grams, 1)
print(weight_in_ounces, "ounces is", weight_in_grams, "grams.")
