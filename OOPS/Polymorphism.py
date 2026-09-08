#2. Polymorphism - one name many forms

#second pillar of OOP

#METHOD OVERRIDING

class Animal:
    def show(self):
        print("Hello")

class Human(Animal):
    def show(self):
        print("Heyy")

obj=Human()
obj.show()

#Duck typing- ig it walks like a duck and quacks like a duck, it must be a duck
class Hello:
    def show(self):
        print("Hello i am showing")

class Hii:
    def show(self):
        print("Hi I am also showing")

obj=Hello()
obj2=Hii()

obj.show()
obj2.show()