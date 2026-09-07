class Factory:
    def __init__(self,material,zips):
        self.material=material
        self.zips=zips

    def show(self):
        print(f"your information in the dunder function is {self.material} and {self.zips}")
        #it will receive value from object of class

Reebok=Factory("leather",2)     #object 1

#Brand=Factory("nylon",3)        #object 2

#print(Reebok.zips)

#print(Brand.material)

Reebok.show()
