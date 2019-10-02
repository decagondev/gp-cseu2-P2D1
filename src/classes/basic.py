# create a basic Animal class add some getter and setter methods
class Animal:
    # constructor
    def __init__(self, name, num_legs):
        self.name = name
        self.num_legs = num_legs
    # methods

    # getters
    def get_name(self):
        return self.name

    def get_legs(self):
        return self.num_legs
    # setters
    def set_name(self, name):
        self.name = name

    def set_legs(self, num_legs):
        self.num_legs = num_legs

# "is a"
class Dog(Animal):
    def __init__(self, breed, num_legs=4):
        self.name = "Dog"
        self.breed = breed
        self.num_legs = num_legs
    
    # getters and setters

    def get_breed(self):
        return self.breed
    
    def set_breed(self, breed):
        self.breed = breed


a = Animal("Bob", 20)
a.name = "Dave"
a.age = 23