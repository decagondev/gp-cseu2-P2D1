from product import Product


class Tool(Product): # Tool "is_a" Product
    def __init__(self, name, weight, price):
        super().__init__(name, price)
        self.weight = weight

    def __str__(self):
        return super().__str__() + f" \t{self.weight}KG"