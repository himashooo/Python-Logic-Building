def fact(n):
    ft=1
    for i in range(1,n+1):
        if n==0 and n==1:
            print(n)
        else:
            ft*=i
    return ft
print(fact(3))