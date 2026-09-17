"""
when you create a decorator , you give parameter,

and function you are creating decorator for is passed as parameter to the decorator function,

"""


def decorate(func): 
    def wrapper(a,b):
        print("Before function execution")
        func(a,b)
        print("After function execution")
    return wrapper


@decorate
def Hello(a,b):
    print(f"Addition is {a+b}")

Hello(5,5)


#decorators with args and kwargs - not touching decorator function, but changing the function which is being decorated

def decorate1(func): 
    def wrapper(*args, **kwargs):
        print("Before function execution")
        func(*args,**kwargs)
        print("After function execution")
    return wrapper


@decorate1
def Hey(a,b,c):
    print(f"Addition is {a+b}")

Hey(5,5,5)