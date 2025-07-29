#Count how many times each character appears in a string (use dictionary).

A="himanshu"
dic={}
for i in A:
    if i in dic:
        dic[i]+=1       #increment count if char exists
    else:
        dic[i]=1        #init count if not found
print(dic)