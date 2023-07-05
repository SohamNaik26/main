import random

def gameWin(Comp, you):
    if Comp == 'S':
        if  you == 'W':
            return None

    elif Comp == 'S':
        if you == 'W':
            return False
        elif you == 'g':
            return True
    elif Comp == 'W':
        if you == 'g':
            return False
        elif you == 'S':
            return True
        elif Comp == 'g':
            if you == 'g':
                return False
            elif you == 's':
                return True


a = input("Comp Turn: Snake(S) Water(W) or Gun(g)?")
randNo = random.randint(1, 3)
print(randNo)

if randNo == 1:
    Comp = "S"

elif randNo == 2:
    Comp = "W"

elif randNo == 3:
    Comp = "g"
you = input("Your Turn: Snake(S) Water(W) or Gun(g)?")

gameWin(Comp, you)
if  a == None:
    print("The game is a tie!")

elif a:
    print("You Win")

else :
    print("You Lose")