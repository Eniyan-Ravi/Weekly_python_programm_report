class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
s1=student("Hela",34)
s2=student("Alice",22)
s1.display()
s2.display()