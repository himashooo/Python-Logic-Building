l="himanshu"
a=[]
unique=True
for i in l:
    if i in a:
        unique=False
        break
    a.append(i)
if unique:
    print("It is unique")
else:
    print("Not")