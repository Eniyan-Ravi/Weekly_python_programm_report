import random 
print("Guess the number between 1-6")
while True:
    x=int(input("Enter the no.:"))
    a=random.randint(1,6)
    print(a)
    if x==a:
        print("You have guessed the no. correct :)")
        break
    else:
        print("Try again")
        print("")