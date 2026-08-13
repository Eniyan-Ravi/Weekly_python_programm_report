n=int(input("Enter the number:"))
x=len(str(n))
arm=sum(int(d)**x for d in str(n))

if n==arm:
    print("The entered no. is armstrong number")
else:
    print("Not an armstron number")