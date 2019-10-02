# create a category class with a name for now 
# and build upon it further in future iterations

class Category:

    # constructor
    def __init__(self, name): #, products)
        self.name = name
    # str
    def __str__(self):
        return "No products available in " + self.name