#Print even and odd numbers separately from a list.

l=[1,5,7,8,9,46,31,33]
even=[]     #stores even no
odd=[]      #stores odd no
for i in l:
    if i%2==0:
        even.append(i)      
    else:
        odd.append(i)
print(f"Even no are = {even}")
print(f"Odd no are={odd}")