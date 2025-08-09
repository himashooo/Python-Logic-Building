def prime(n):
    is_prime=True
    if n>1:
        for i in range(2,n):
            if n%i==0:
                is_prime=False
                break
        if is_prime:
            print("its a prime no")
        else:
            print("not a prime no")
    else:
        print("Not a prime")
print(prime(8))