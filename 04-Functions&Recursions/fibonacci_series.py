#Write a function that returns the Fibonacci sequence up to n terms.

def fib(n):
    a=1
    for i in range(1,n+1):          #loop 1 to n+1
        a*=i
    return a            #returns fibonacci sequence
print(fib(3))