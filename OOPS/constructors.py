class Factory:
    def __init__(self,material,zips):
        self.material=material
        self.zips=zips


Reebok=Factory("leather",2)

Brand=Factory("nylon",3)

print(Reebok.zips)

print(Brand.material)