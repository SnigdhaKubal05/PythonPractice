"""
Dunder methods are special method starts and ends with double underscore

dunder itself means double underscore
they automatically gets called when you perform ertain action on an object

eg.: __init__

"""

class Animal:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f"Hi my name is {self.name}"

object=Animal("Snigdha")

print(object)

"""
when you print object it directly access the dunder methods (when using 'return')
"""

#addition of object 
class Addition:
    def __init__(self,age):
        self.age=age

    def __add__(self, other):       #self is first thing you want to add and other is second thing you want to add
        return f"Addition of your age is {self.age + other.age}"

object=Addition(20)
object1=Addition(40)


print(object+object1)


#trying to add 3 objects using Tuple
class Add:
    def __init__(self,age1):
        self.age1=age1

    def __add__(self, other):   #self is first thing you want to add and other is second thing you want to add
        sum=0
        for i in other:      
            sum=sum+i.age1
        return f"Addition of your age is {self.age1 + sum}"

obj1=Add(20)
obj2=Add(40)
obj3=Add(20)

print(obj1 + (obj2,obj3))