#programming paradiagm based on the concept of objects

class Factory:
    #local scope
    attribute1=12           #this is attribute - variable inside a class

    def hello(self):            #this is method - a function inside a class
        #self ke andar oject ki LOCATION save hoti hai
        print("Snigdhaa")

    #open statement
    print("Initializing the class")

"""
print(Factory.attribute1)
Factory.hello()
"""

# OBJECTS creation

obj=Factory()
print(obj.attribute1)
obj.hello()