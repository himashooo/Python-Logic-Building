#Reverse a list without using the reverse() function.

list=["india","england","usa","japan"]
rev=[]
for i in list[-1:-5:-1]:        # iterate from last to first
    rev.append(i)
print(rev)