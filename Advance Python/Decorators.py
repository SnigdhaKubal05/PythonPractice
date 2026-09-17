"""
when you create a decorator , you give parameter,

and function you are creating decorator for is passed as parameter to the decorator function,

"""


def decorate(func): 
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper


@decorate
def Hello():
    print("Hello i am showing in function Hello()")

Hello()