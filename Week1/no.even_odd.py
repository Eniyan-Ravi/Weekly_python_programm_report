#finding no. of even and odd
a=[1,2,3,4,5,6,7,8]
even=0
odd=0
for x in a:
    if x%2==0:
        even+=1
    else:
        odd+=1
print("No. of even",even)
print("No.of odd",odd)