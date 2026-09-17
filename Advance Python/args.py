"""
jab bhi hum decorators ka use karte hai 
we have to mention the parameters which we want to pass to the decorator function.


but we might not know how many parameters we want to pass to the decorator function.

so we can make use of *args and **kwargs to pass any number of parameters to the decorator function.

all this because we dont know how many argguments user will give.

"""

#args---> arguments ---- tuples
#kwargs---> keyword arguments ---- dictionary -- does not work in Positions

def add(*args):
    sum=0
    for i in args:
        sum+=i

    print(f"Addition is {sum}")


add(1,2,3,4,5)

#kwargs -- dictionary

def information(**kwargs):
    print("Information is as follows")

    for i in kwargs:
        print(f"{i}: {kwargs[i]}")

    #print(kwargs)

information(a=12,b=6)