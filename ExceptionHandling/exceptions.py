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

