#Create a Vehicle → Car and Bike inheritance example.
class Vehicle:

    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def car_info(self):
        print("Car details")
        print("Car Brand:", self.brand)
        print("Car Model:", self.model)


class Bike(Vehicle):

    def __init__(self, brand, bike_type):
        self.brand = brand
        self.bike_type = bike_type

    def bike_info(self):
        print("Bike details")
        print("Bike Brand:", self.brand)
        print("Bike Type:", self.bike_type)


c = Car("BMW", "M4")

b = Bike("Yamaha", "R15")

c.start()
c.car_info()

b.start()
b.bike_info()