class One:

    attribute1=29           #class attribute

    def __init__(self,age):
        self.age=age        #instance attribute

    #instance method
    def show(self):         #instance method because accepting self.- because it targets object location
        print(f"SNIGDHAA {self.age}")   #we can use instance attribute like this

    #class method
    @classmethod
    def hello(cls):         #'clsc' targets class location
        #can also write self but we are not targeting object location here
        print("SNIGDHAA2")

    
    #static method
    @staticmethod
    def static():
        print("SNIGDHAA3")


obj=One("22")
obj.show()
obj.hello()
obj.static()

#normal method without show or decorator will give error