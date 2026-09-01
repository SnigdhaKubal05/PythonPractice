a=int(input("enter your number: "))
try:
    print(10//a)

except Exception as err:        #its like IF, if this does not runs ELSE block will run
    print(f"sorry lol, enter valid number and not {err}")

#OR

else:                           #runs only if there us not exception
    print("There is no exception")

finally:
    print("I will run no matter what")


print("Will run anyway")

#Raise - manually throwing exception

age=int(input("Enter you age: "))
try:
    if age<10 or age>18:
        raise ValueError("your age must be between 10 and 18")
    else:
        print("Welcome to the club")
except Exception as err:
    print(f"An error occured as {err}")

print("club opening soon")