# Create a store class with a name and categories
# fields name, categories

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
            output += "  " + str(i) + ". " + c + "\n"
            i += 1
        return output

s = Store("Bob's Store", ["Shoes", "Hats", "Hellicopters"])

print(s)
selection = input("Select the number of the department.")

print("The user selected " + str(selection))