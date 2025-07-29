#Check whether a number is a palindrome or not (e.g., 121 is a palindrome).

n=int(input("enter a number: "))
x=n                             #store original no
rev=0
while(n>0):
    rev=(rev*10)+n%10           #add last digit to rev
    n=n//10                     #remove last digit from n
print("Rev",rev)
if rev==x:                        #compare rev or original
    print("it is a palindrome")
else:
    print("Not a palindrome")