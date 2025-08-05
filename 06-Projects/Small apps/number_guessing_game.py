import random
def guess_():
    rand_int=random.randint(1,20)
    Attempts_=0
    while True:
        n=int(input("Guess a integer : "))
        diff_=rand_int-n
        close_pos=(1,2,3,4,5)
        close_neg=(-1,-2,-3,-4,-5)
        if n==rand_int:
            print("You guessed it right")
            break
        elif diff_ in close_pos:
            print("Very close but Little High")
        elif diff_ in close_neg:
            print("Very close but Little Low")
        elif n>rand_int:
            print("Too High")
        elif n<rand_int:
            print("Too Low")
        else:
            print("Invalid input")
        Attempts_+=1
        print(f"Attempt no = {Attempts_}")
    print(f"Total no of attemps={Attempts_}")
guess_()