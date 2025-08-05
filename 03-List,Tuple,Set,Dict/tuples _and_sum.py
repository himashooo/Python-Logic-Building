#Create a tuple of 10 numbers and find their sum.

l=()
for i in range(1,11):
    n=int(input("enter a number"))
    l=list(l)
    l.append(n)     # add to list
    l=tuple(l)      # convert back to tuple
print(l)
sum_=sum(l)     # calculate sum
print(f"sum={sum_}")