# create a Motor class and create a Car class that "Has A" Motor

class Motor:
    def __init__(self, make, cc):
        self.make = make
        self.cc = cc

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine
        
honda_petrol_motor = Motor("Honda", 1799)
car = Car("Honda", "Civic", honda_petrol_motor)

print(car.engine.cc)