#Check if a string contains all unique characters.

l="himanshu"
a=[]
unique=True
for i in l:
    if i in a:              #If char already seen not unique
        unique=False
        break
    a.append(i)
if unique:
    print("It is unique")
else:
    print("Not")