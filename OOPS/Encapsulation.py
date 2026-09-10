#oly showing necessary parts of the code, and controlling the access
#we use access modifiers to control the access of attributes and methods of a class from object and inherited classes

#all the attributes and methods are public, 

#protected: use "_" one underscore -------> although it works like public class only

#private: use "__" double underscore ----->nothing can access private attributes and methods, no object and inherited classes


class Factory:
    __a="pune"

    def show(self):
        print("I am Pune class")

        print(Factory.__a)      #we can access private attributes like this but cannot change

"""class Bhopal(Factory):
    def show(self):
        print(super().__a)

obj=Bhopal()
obj.show()"""

obj1=Factory()
obj1.show()


#Example 2
class Demo:
    def __init__(self):
        self.name="Public"             #public
        self._age=20                    #protected
        self.__salary=50000             #private

    def show(self):
        print("inside the class: ")
        print("Public: ",self.name)
        print("Protected: ", self._age)
        print("Private: ",self.__salary)

object=Demo()
object.show()