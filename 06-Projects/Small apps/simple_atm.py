print("\t ATM")
print("1=Check balance\n2=Withdrawl\n0=Exit")
Amount=100000
limit=0
while True:
    Option=int(input("Enter an option: "))
    if Option==1:
        print(f"Current Balance {Amount} rs")
    elif Option==2:
        if limit!=3:
            wdrwl=int(input("Enter Withdrawl Amount: "))
            if wdrwl>Amount:
                print("Insufficient balance")
            elif wdrwl<=0:
                print("Invalid amount entered")
            elif wdrwl>20000:
                print(f"No withdrawls more than 20000rs")
            else:
                Amount-=wdrwl
                limit+=1
                print(f"Remaining Balance = {Amount}rs\nWithdrawls left={3-limit}")
        else:
            print("Withdrawl limit exceeded")
    elif Option==0:
        print("Thank you for using Himashoo's ATM")
        break
    else:
        print("Invalid Option")