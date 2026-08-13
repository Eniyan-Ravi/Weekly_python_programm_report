#Build an Online Shopping hierarchy with Product, Electronics, and Clothing classes.
class Product:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Product Name:", self.name)


class Electronics(Product):

    def __init__(self, name, brand):
        super().__init__(name)
        self.brand = brand

    def display_electronics(self):
        print("Electronics")
        self.display()
        print("Brand:", self.brand)


class Clothing(Product):

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def display_clothing(self):
        print("Clothing")
        self.display()
        print("Size:", self.size)


e = Electronics("Laptop", "Acer")
c = Clothing("Shirt", "XL")

e.display_electronics()

print()

c.display_clothing()