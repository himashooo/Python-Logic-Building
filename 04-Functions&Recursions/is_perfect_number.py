n=6
a=[]
for i in range(1,n):
    if n%i==0:
        a.append(i)
if sum(a)==n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")