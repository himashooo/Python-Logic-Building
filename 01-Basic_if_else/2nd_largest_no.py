def xyz(l):
    L=list(set(l))
    if len(L)<2:
        return None
    L.sort()
    return L[-2]
l=[1,2,2,3,5,6,10,4]
print("Secong largest no =", xyz(l))
