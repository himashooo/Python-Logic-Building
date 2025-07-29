string_="himanshu"
checked=[]                        #to store already counted char
for i in string_:
    if i not in checked:
        c=0
        for j in string_:
            if i==j:
                c+=1
            print(f"{i}={c}")
            checked.append(i)       #marked this char as checked