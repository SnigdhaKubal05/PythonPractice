"""#there are 4 pillars of OOP 

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

class Animal:       #parent/super class
    def __init__(self, name):
        self.name=name

    def show(self):
        print(f"name is {self.name}")

class Human(Animal):    #child/sub class
    def __init__(self, name,age):
        super().__init__(name)      #targets constructor of Super/parent class

        self.age=age

    def show(self):     #method overriding
        print(f"name is {self.name} and age is {self.age}")


AnimalObj=Animal("Lion")    #instance of parent

HumanObj=Human("Snigdha",20)   #instance of child

HumanObj.show()

#AnimalObj.show()

#multiple inheritence

class Parent1:
    name1="Parent1"

    def __init__(self,name):
        pass

class Parent2:
    name2="Parent2"

    def __init__(self,name,age):
        pass

class Child(Parent2,Parent1):       #Method Resolution Order (MRO)
    name3="Child"

object1=Child()

print(object1.name2)"""

#Multilevel Inheritence

class Grandparent:
    def __init__(self,name):
        self.name=name

class Parent(Grandparent):
    def __init__(self,name,age):
        super().__init__(name)

        self.age=age

class Child(Parent):
    def __init__(self, name, age, degree):
        super().__init__(name, age)

        self.degree=degree

    def show(self):
        print(f"{self.name}, {self.age} and {self.degree}")

object=Child("Snigdha",20,"BCA")

object.show()


