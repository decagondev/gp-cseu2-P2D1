# Create a store class with a name and categories
# fields name, categories
from category import Category
from product import Product
from tool import Tool

class Store:
    # constructor
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories
    # methods
    def __str__(self):
        output = ""
        output += self.name + "\n"
        i = 1
        for c in self.categories:
            output += "  " + str(i) + ". " + c.name + "\n"
            i += 1
        
        # add an exit message
        output += "  " + str(i) + ". Exit"
        return output

s = Store("Bob's Store", [Category("Shoes", []), Category("Hats", [Tool("Hammer", 1000, 6000.67)]), Category("Hellicopters", [Product("Generic Product", 5000.60)]), Category("Belts", [Product("Generic Product", 5000.60)])])

print(s)
selection = 0

while selection != len(s.categories) + 1:
    selection = input("Select the number of the department.")
    try:
        selection = int(selection)
        if selection == len(s.categories) + 1:
            print(f"Thanks for shopping at {s.name}")
        elif selection > 0 and selection <= len(s.categories):
            print(s.categories[selection - 1])
        else:
            print("Select a valid number!")
    except ValueError:
        print("Please enter your choice as a number")