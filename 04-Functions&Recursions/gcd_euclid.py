def gcd(a,b):
    factor1=[]
    factor2=[]
    common=[]
    for i in range(1,a):
        if a%i==0:
            factor1.append(i)
    print(f"Factors of a={factor1}")
    for j in range(1,b):
        if b%j==0:
            factor2.append(j)
    print(f"Factors of b={factor2}")
    common=set(factor1) & set(factor2)
    print(common)
    c=max(common)
    print(c)
    
gcd(12,18)