#Guessing (hand cric)
import random 
print("Welcome!")

def toss(t):
    if t == 't' or t=='T':
        to=2
    elif t == 'H' or t=='h':
        to=1   
    else:
        print("Give correct input") 
        to=3
    toss_rand=random.randint(1,2)
    if to == toss_rand:
        print("You have won the toss!")
        return True
    else:
        print("You lost the toss :<|")
        return False
    
over=int(input("Chosses no. of over:"))

t=input("Chose H or T:")
result=toss(t)

def select(result):
    if result==True:
        a=input("Select bat or bowl first!(B-bat,BO-bowl):")
        side_sele=a.lower()

        if side_sele == 'b':
            print("You bat first!")
            print("")
            bat_f(over)
        elif side_sele == 'bo':
            print("you bowl first!")
            print("")
            bow_f(over)
    else:
        tos_res=random.randint(1,2)
        if tos_res==1:
            print("You bat first!")
            print("")
            bat_f(over)
        else:
            print("You bowl first!")
            print()
            bow_f(over)


def bat_f(over):
    run=0
    print("You bat first ;)")
    for x in range(6*over):
        sys_bowl=random.randint(1,6)
        print("")
        print("Ball no. ",x+1)
        user_bat=int(input("Enter the val:"))
        if user_bat!=sys_bowl:
            print("Sys val.:",sys_bowl)
            run+=user_bat
            print("your run:",run)
        elif user_bat==sys_bowl:
            print("You are out!")
            print(run)
            break
    

    run_2=run
    run_over=0
    print("")
    print("NPC bating ;|")
    for x in range(6*over):
            sys_bat=random.randint(1,6)
            print("")
            print("Ball no. ",x+1)
            user_bow=int(input("Enter the val:"))
            
            if user_bow == sys_bat:
                print("NPC is out!")
                print("You won by ",run_2-run_over," runs")
                break
            print("Sys val.:",sys_bat)
            run_over+=sys_bat
            print("NPC run:",run_over)
            

            if run_over > run_2:
                print("")
                print("NPC won")
                break
    else:
        if run_over >run_2:
            print("NPC won")
        elif run_over < run_2:
            print("You won by ",run_2-run_over," runs")
        else:
            print("Match tied")



def bow_f(over):
    run=0
    for x in range(6*over):
        sys_bat=random.randint(1,6)
        print("")
        print("Ball no. ",x+1)
        user_bow=int(input("Enter the val:"))
        if user_bow!=sys_bat:
            print("Sys val.:",sys_bat)
            run+=sys_bat
            print("NPC run:",run)
        elif user_bow==sys_bat:
            print("NPC is out!")
            print("NPC run:",run)
            break
    
    run_2=run
    run_over=0
    print("")
    print("You are batting ;>")
    for x in range(6*over):
        sys_bow=random.randint(1,6)
        print("")
        print("Ball no. ",x+1)
        user_bat=int(input("Enter the val:"))
                
        if user_bat==sys_bow:
            print("You is out!")
            print("NPC won by ",run_2-run_over," runs")
            break
        print("Sys val.:",sys_bow)
        run_over+=sys_bow
        print("Your run:",run_over)
        print("Needed runs:",run_2-run_over)

        if run_over>run_2:
            print("")
            print("NPC Lost")
            print("You won")
            break
    else:
        if run_over >run_2:
            print("NPC won")
        elif run_over < run_2:
            print("You won by ",run_2-run_over," runs")
        else:
            print("Match tied")

select(result)


