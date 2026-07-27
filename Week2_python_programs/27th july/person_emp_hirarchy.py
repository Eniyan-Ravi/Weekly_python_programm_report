#Create a Person → Employee → Manager inheritance hierarchy.
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):

    def __init__(self, name, age, emp_id):
        self.name = name
        self.age = age
        self.emp_id = emp_id

    def display_employee(self):
        print("Employee ID:", self.emp_id)


class Manager(Employee):

    def __init__(self, name, age, emp_id, department):
        self.name = name
        self.age = age
        self.emp_id = emp_id
        self.department = department

    def display_manager(self):
        print("Department:", self.department)


m = Manager("Eniyan", 22, 101, "trainee")

m.display_person()
m.display_employee()
m.display_manager()