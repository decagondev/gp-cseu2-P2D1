# gp-cseu2-P2D1
OOP Python Day 1 Guided Project for CSEU2

## Challenge Submissions

*Jakub Maleta*

```python
class Cat(Animal):
  def __init__(self, name, color, breed):
    super().__init__(name, 4)
    self.color = color
    self.breed = breed

  def get_color(self):
    return self.color

  def get_breed(self):
    return self.breed

  def set_color(self, color):
    self.color = color

  def set_breed(self, breed):
    self.breed = breed
```

*Wasiu Idowu*

```python
class Bird(Animal):
    def __init__(self, breed, num_legs=2):
        self.name = 'Bird'
        self.breed = breed
        self.num_legs = num_legs

    def getBreed(self):
        return self.breed

    def getLegs(self):
        return self.num_legs

    def setBreed(self, breed):
        self.breed = breed

    def setLegs(self, num_legs):
        self.num_legs = num_legs



pigeon = Bird('African Owl Pigeon', 2)
print(pigeon.getBreed())
pigeon.setLegs(3)
print(pigeon.getLegs())
```

*Haja Andriamaro*

```python
class Bird(Animal):
    def __init__(self, name, num_legs, flight_dist, num_wings):
        super().__init__(name, num_legs)
        self.flight_dist = flight_dist
        self.num_wings = num_wings
```