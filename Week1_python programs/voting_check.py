age=int(input("Enter your age:"))
if age>=18:
    print("You are eligible to vote :)")
elif age<18 and age>0:
    print("You are not eligible to vote :()")
else:
    print("Please enter a valid input")
    