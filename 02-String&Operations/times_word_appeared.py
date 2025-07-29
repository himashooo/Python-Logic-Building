l="Hey himanshu,how are you himanshu,where do you live Himanshu"
n="himanshu"
c=0
words=l.lower().replace(","," ").split()  #Convert to lowecase,remove commas,split to words
print(words)
for i in words:
    if i == n:
        c+=1
print(c)