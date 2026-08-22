#functions
#positional arguements
def sum(a,b):  #parameters
    print(f"sum of your number is {a+b}")

sum(2,2) #arguements
sum(5,5)

#default arguements
def sum(x,y=5):  #parameters
    print(f"sum of your number is {x+y}")

sum(2) 

#keyword arguements
def key(name,age):
    print(f"your name is {name} and age is {age}")

key(age=20,name="snigdha")