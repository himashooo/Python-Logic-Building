#Use recursion to calculate the power of a number (x^y).

def power(x,y):
    if y==0:        #base case
        return 1
    else:
        return x*power(x,y-1)       #recursive step
print(power(2,3))