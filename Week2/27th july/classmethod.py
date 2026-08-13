#class method
class student:
    school="Hi school"
    @classmethod
    def showschool(cls):
        print(cls.school)

student.showschool()