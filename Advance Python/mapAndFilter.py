"""

map()---> it takes two parameters - function and iterable.
It applies the function to each item in the iterable and returns a map object (which is an iterator). 

"""

#with lambda function
l=[1,2,3,4,5]

result=map(lambda x: x+1, l)
print(list(result))


#with normal function

a=[1,2,3,4,5]
def addition(x):
    return x+1

result=map(addition,a)

print(list(result))

"""
filter()---> it takes two parameters - function and iterable.
takes a sequence like list, tuples etc
filter() passes each item in the iterable to the function and
returns only those items for which the function returns True.

"""

#with lambda function

a=[1,2,3,4,5]

result2=filter(lambda x: True if x%2==0 else False,a)

print(list(result2))


#with normal function

def even(x):
    if x%2==0:
        return True
    else:
        return False

result1=filter(even,a)

a=[1,2,3,4,5]

print(list(result1))