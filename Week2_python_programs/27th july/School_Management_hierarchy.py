#Build a School Management hierarchy with Person, Teacher, and Student
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Teacher(Person):

    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def display_teacher(self):
        self.display_person()
        print("Subject:", self.subject)


class Student(Person):

    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def display_student(self):
        self.display_person()
        print("Roll Number :", self.roll_no)


t = Teacher("Ramesh", 40, "Math")
s = Student("Eniyan", 22, 101)

print("Teacher Details")
t.display_teacher()

print("Student Details")
s.display_student()