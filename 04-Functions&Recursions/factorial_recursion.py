#Find the factorial using recursion.

def fact_(n):
       if n==0 or n==1:          #base case
        return 1
       else:
          return n*fact_(n-1)    #recursive call
            
print(fact_(5))