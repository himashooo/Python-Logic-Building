#Find the second largest number in a list.

def xyz(l):
    L=list(set(l))          #removes duplicates
    if len(L)<2:
        return None
    L.sort()                #sort in ascending order
    return L[-2]
l=[1,2,2,3,5,6,10,4]
print("Secong largest no =", xyz(l))
