#Write a program to create a class Vehicle and perform the following tasks - 1. Create an __init__ method with arguments - max_speed and mileage 2. Create an object of class Vehicle and pass the maximum speed and mileage of the car 3. Print the values of max_speed and mileage by using the object

class vehicle:
    def __init__(self,mileage,max_speed):
        self.mileage=mileage
        self.max_speed=max_speed

obj=vehicle(100,70)
print("Max speed is",obj.max_speed)
print("Mileage is",obj.mileage)
