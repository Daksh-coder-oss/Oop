class Parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj=Parrot("Bobo",8)
print(obj.species,obj.name,obj.age)
        