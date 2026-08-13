#variable lengith position argument
def student(name, *marks):

    print("Name:", name)

    print("Marks:", marks)

student("Alice", 90, 85, 95)
#variable lengith keyword argument 

def student(**details):

    print(details)

student(name="Alice",
        age=22,
        city="Chennai")