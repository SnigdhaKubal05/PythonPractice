#programming paradiagm based on the concept of objects

class Factory:
    #local scope
    attribute1=12           #this is attribute - variable inside a class

    def hello():            #this is method - a function inside a class
        print("Snigdhaa")

    #open statement
    print("Initializing the class")

print(Factory.attribute1)
Factory.hello()

