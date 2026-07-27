a=[2,4,7,5,1,3]
sum=int(input("Enter the sum:"))

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==sum:
            print(a[i],",",a[j])