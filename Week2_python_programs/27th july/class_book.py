#create class book and display details of multimple book
class Book:
    def __init__(self,b_name,b_author,b_price):
        self.b_name=b_name
        self.b_author=b_author
        self.b_price=b_price

    def display(self):
        print("Book Title:",self.b_name)
        print("Author name:",self.b_author)
        print("Price:",self.b_price)
        print("")


b1=Book("Goosebumps","R.L.Stain",450)
b2=Book("Gernimouse Stilton","Jeffri Nicole",380)
b3=Book("Solo Leveling","Kenjiro Tuda",550)
b1.display()
b2.display()
b3.display()
