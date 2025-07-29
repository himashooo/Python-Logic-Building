A="himanshu"
dic={}
for i in A:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)