#there are 4 pillars of OOP 

#1. Inheritance
class Parent:
    attribute1="I am attribute, inside parent class"

    def method1(self):
        print("Hi i am emthod, inside parent class")

class Child(Parent):
    pass

object1=Parent()

object2=Child()

print(object1.attribute1)

print(object2.attribute1)

object2.method1()

#all the attributes and methods can be access using object of child class as well.

#Contructor Inheritence

class Animal:
    def __init__(self, name):
        self.name=name

    def show(self):
        print(f"name is {self.name}")

class Human(Animal):
    pass

HumanObj=Human("Snigdha")

AnimalObj=Animal("Lion")

HumanObj.show()

AnimalObj.show()