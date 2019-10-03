# create a category class with a name for now 
# and build upon it further in future iterations

class Category:

    # constructor
    def __init__(self, name, products):
        self.name = name
        self.products = products
    # str
    def __str__(self):
        output = "  " + self.name + "\n"
        if len(self.products) < 1:
            output = "No products available in " + self.name
        for p in self.products:
            output += "    " + str(p) + "\n"

        return output