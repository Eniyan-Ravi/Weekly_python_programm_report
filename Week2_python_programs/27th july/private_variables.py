#private_variables
class Student:

    def __init__(self):
        self.__name = "Eniyan"

    def display(self):
        print(self.__name)

s = Student()
s.display()