#Create a tuple of 10 numbers and find their sum.

l=()
for i in range(1,11):
    n=int(input("enter a number"))
    l=list(l)
    l.append(n)
    l=tuple(l)
print(l)
sum_=sum(l)
print(f"sum={sum_}")