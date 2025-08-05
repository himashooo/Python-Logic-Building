to_do_list=[]
print("Enter '1' for Add\nEnter '2' for Remove\nEnter '3' for Stop")
while True:
    try:
        Task_=int(input("Enter a no 1-3: "))
        if Task_==1:
            n=input("Add a to do work: ").upper()
            to_do_list.append(n)
            print(to_do_list)
        elif Task_==2:
            print(to_do_list)
            if not to_do_list:
                print("Nothing To remove 'EMPTY LIST' ")
            else:
                n=input("Remove a to do work: ").upper()
                to_do_list.remove(n)
                print(to_do_list)
        elif Task_==3:
            break
        else:
            print("Invalid integer")
    except ValueError:
        print(f"Invalid input {ValueError}")
print(f"Your TO DO LIST\n{to_do_list}")