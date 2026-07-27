class employee:

    def __init__(self, e_name, e_id, e_age, e_gender):
        self.e_name = e_name
        self.e_id = e_id
        self.e_age = e_age
        self.e_gender = e_gender

    def display(self):
        print(self.e_name)
        print(self.e_id)
        print(self.e_age)
        print(self.e_gender)

s = employee("Eniyan", 575, 22, "male")
s.display()