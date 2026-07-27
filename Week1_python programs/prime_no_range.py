n=int(input("Enter the number:"))
if n==1:
    print("No.is neither prime nor composite")
else:
    y=False
    for x in range(2,n):
        if n%x==0:
            y=True
    if y==False:
        print("The no. is prime")
    else:
        print("The no. is not prime")