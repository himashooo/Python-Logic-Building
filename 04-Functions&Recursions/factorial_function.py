#Create a function that takes a number and returns its factorial.

def fact(n):
    ft=1
    for i in range(1,n+1):
        if n==0 and n==1:       #checks for base case
            print(n)
        else:
            ft*=i           #multi current value to factorial
    return ft
print(fact(3))