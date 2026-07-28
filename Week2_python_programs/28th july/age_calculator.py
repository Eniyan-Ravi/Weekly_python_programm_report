#age cal 
from datetime import datetime

dob = input("Enter your DOB (dd-mm-yyyy): ")

birth = datetime.strptime(dob, "%d-%m-%Y")
today = datetime.now()

age = (today - birth).days // 365
print("Days:",(today-birth).days)
print("Age:", age, "years")