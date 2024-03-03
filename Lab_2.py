##
#A file for lab 2 for my code on code runner
import math

# starter sheet
radius = input("Enter the radius: ")
area = math.PI * radius ** 2
print("Area is", area)

#Q1
base = 45
height = 20
area = base * height / 2
print("area", area)

#Q2
radius = 10
area = 3.14159265359 * radius ** 2
print("Area of circle", area)

#Q3
name = input("Enter your name: ")
print("Hello", name)
print("Goodbye", name)

#Q4
name = input("Enter your name: ")
age = int(input("Enter your age: "))
current_year = int(input("Enter the current year: "))
year_of_birth = current_year - age
future_year = int(input("Enter a future year: "))
future_age = future_year - current_year + age
print("My name is", name, "and I was born in", year_of_birth)
print("I will be", future_age, "in", future_year)

#Q5
cny_to_nzd = 0.22
amount = float(input("Enter an amount in NZD: "))
cny = round(amount / cny_to_nzd, 2)
print(amount, "NZD is equivalent to", cny ,"CNY")

#Q6
n = int(input("Enter the value for n: "))
first_part_of_equation = (n*(n+1))
second_part_of_equation = first_part_of_equation * (2 * n + 1)
final_part_of_equation = round(second_part_of_equation / 6)
print("The sum of the first", n, "squared integers is", final_part_of_equation)

#Q7
people = int(input("Enter the number of people: "))
slices_in_each_cake = int(input("Enter the number of slices in each cake: "))
cakes_needed = math.ceil(people / slices_in_each_cake)
print(cakes_needed, "cakes are needed.")

#Q8
adjacent = float(input("Enter the length of the adjacent side: "))
θ = float(input("Enter the value of the angle: "))
angle = math.cos(θ)
hypotonuse = round(adjacent / angle, 3)
print("The length of the hypotenuse is", hypotonuse)

#Q9: period=2π√L/g
g = 9.8066
length = float(input("Enter the length of the pendulum in metres: "))
square_root = math.sqrt(length / g)
period = round(2 * math.pi * square_root, 2)
print("The period of the pendulum is", period,"seconds.")

#Q10 math.floor()
total_seconds =int(input("Enter the total number of seconds: "))
hours = (total_seconds // 3600)
minutes = (total_seconds - hours * 3600)// 60
seconds = (total_seconds - hours * 3600 - minutes * 60)
print(total_seconds, "second(s) is equal to", hours, "hour(s),", minutes, "minute(s), and", seconds, "second(s).")

#Q11
one_drink = 200
large_contaier_drinks = 65
large_container_mls = large_contaier_drinks * one_drink
people = int(input("Enter the number of people: "))
drinks = people % large_contaier_drinks
drinks_wasted = (large_contaier_drinks - drinks) % large_contaier_drinks
mls_wasted = drinks_wasted * one_drink
print(drinks_wasted, "drinks (" + str(mls_wasted) + "ml) are wasted.")
