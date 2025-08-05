#Find the average of elements in a list.

l=[1,4,5,8,9,3]
avg=0
for i in l:
    avg+=i          #adding each no to avg
avg/=len(l)         #divide sum by count to get average
print(avg)

       #OR (simpler)

"""l2=[1,4,5,8,9,3]
avg_=sum(l2)/len(l2)
print(avg_)"""