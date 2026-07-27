#Rotate Array by K Positions
a=[4, 5, 1, 2, 3]
k=int(input("Enter the no.:"))
print(a)
for i in range(k):
    x=a.pop()
    a.insert(0,x)
print(a)