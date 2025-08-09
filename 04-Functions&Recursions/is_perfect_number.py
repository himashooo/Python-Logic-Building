#Check if a number is perfect (sum of divisors = number).

n=6
a=[]
for i in range(1,n):
    if n%i==0:              #if i is a divisor
        a.append(i)
if sum(a)==n:               #perfect number condition
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")