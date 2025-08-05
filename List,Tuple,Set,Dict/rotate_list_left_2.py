#Rotate a list to the left by 2 positions.

l=[1,2,3,4,5,6]
rotate_=l[-2:]+l[:-2]       # move last 2 elements to front
print(rotate_)