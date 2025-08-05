#Given a list of numbers, remove all duplicates and print unique values.

l=[1,2,3,4,5,6,1,2,3]
u=[]
for i in l:
    if i in u:
        pass #does nothing in if (imp concept)
    else:
        u.append(i)     # add unique value
print(u)

                       #or

a=[1,2,3,4,5,6,1,2,3]
c=set(a)
a=list(c)
print(a)