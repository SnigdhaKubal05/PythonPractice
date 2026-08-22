
#Q1. Accept 2 numbers and print greatest between them
"""
num1=int(input("Enter first number: "))
num2=int(input("Enter second number "))

if num1>num2:
    print(f"{num1} is greater than {num2}")
elif num2>num1:
    print(f"{num2} is greater than {num1} ")
else:
    print(f"{num1} and {num2} both are equal ")

"""

#Q2. Accept the gender char and print greeting message according to gender char

gender=input("Enter your gender character (M or F): ")

if gender =="M" or gender == "m":
    print("Hello sir!")

elif gender=="F" or gender=="f":
    print("Hello ma'am!")
else:
    print("Enter gender character")