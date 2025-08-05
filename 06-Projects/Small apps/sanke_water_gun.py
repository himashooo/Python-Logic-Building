import random

comp=[1,2,3]
a={1:"snake",2:"water",3:"gun"}
comp_score=0
my_score=0

while comp_score!=3 and my_score!=3:
    n=int(input("choose 1=snake ,2=water ,3=gun : "))

    if n not in [1, 2, 3]:
        print("Invalid input! Choose 1, 2 or 3.")
        continue
    c=random.choice(comp)
    print(f"computer chooses {c}={a[c]}")
    
    if c==n:
        print("draw")

    elif (c == 1 and n == 2) or (c == 2 and n == 3) or (c == 3 and n == 1):
        print("Computer wins")
        comp_score += 1

    else:
        print("You win")
        my_score += 1   
    print(f"MY SCORE ={my_score}\nCOMPUTER SCORE ={comp_score}")
if my_score==3:
    print("\nYOU WON THE GAME")
else:
    print("\nCOMPUTER WON THE GAME")