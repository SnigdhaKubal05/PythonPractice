# we have to import some library to use Abstraction in python
"""
Abstract classes: contains one or more abstract methods
a method that is defined but not implemented in the abstract class.

why to use?: for having common interface for different subclasses

subclasses must provude implementation

example given below

"""

from abc import ABC, abstractmethod

class abstract(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(abstract):
    def __init__(self,side):
        self.side=side

class Circle(abstract):
    def __init__(self,radius):
        self.radius=radius


    #creation of abstract method as we inherit abstract class
    def perimeter(self):
        print("Perimeter")

    def area(self):
        print("Area")

#object
object=Circle(7)
