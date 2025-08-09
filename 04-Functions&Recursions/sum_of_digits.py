#Find the sum of digits of a number (e.g., 123 = 1+2+3 = 6).

def sum(n):
    total=0
    for i in str(n):
        total+=int(i)           #type casting it to int and then adding
    return total        #returns sum of digits
print(sum(426))