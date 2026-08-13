print("Calculater")
a=float(input("Enter the first no.:"))
b=float(input("Enter the second no.:"))
print("Select the operation to be performed:")
print("1.Addition")
print("2.Subtraction")
print("3.Mutiplication")
print("4.Division")
c=int(input("Enter:"))
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4:
    print(a/b)
else:
    print("Invalid input, Enter between 1-4")
    