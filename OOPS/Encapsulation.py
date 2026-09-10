#oly showing necessary parts of the code, and controlling the access
#we use access modifiers to control the access of attributes and methods of a class from object and inherited classes

#all the attributes and methods are public, 

#protected: use "_" one underscore -------> although it works like public class only

#private: use "__" double underscore ----->nothing can access private attributes and methods, no object and inherited classes

class Factory:
    __a="pune"

    def show(self):
        print("I am Pune class")

class Bhopal(Factory):
    def show(self):
        print(super().__a)

obj=Bhopal()
obj.show()