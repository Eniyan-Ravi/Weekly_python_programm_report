#Creating class to cal the average of marks scored by a student
class student:
    def __init__(self,name,math_marks,sci_marks,eng_marks):
        self.name=name
        self.math_marks=math_marks
        self.sci_marks=sci_marks
        self.eng_marks=eng_marks

    def avg(self):
        sum=self.math_marks+self.sci_marks+self.eng_marks
        return sum/3
s=student("Eniyan",66,63,42)
print(s.avg())