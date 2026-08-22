
#Q1. Accept 4 numbers and print greatest between them

num1=int(input("Enter first number: "))
num2=int(input("Enter second number "))
num3=int(input("Enter third number "))
num4=int(input("Enter fourth number "))

if num1>num2 and num1>num3 and num1>num4:
    print(f"{num1} is greater!")

elif num2>num1 and num2>num3 and num2>num4:
    print(f"{num2} is greater!")

elif num3>num1 and num3>num2 and num3>num4:
    print(f"{num3} is greater!")
else:
    print(f"{num4} is greater! ")


"""
#Q2. Accept the gender char and print greeting message according to gender char

gender=input("Enter your gender character (M or F): ")

if gender =="M" or gender == "m":
    print("Hello sir!")

elif gender=="F" or gender=="f":
    print("Hello ma'am!")
else:
    print("Enter gender character")

    
"""

