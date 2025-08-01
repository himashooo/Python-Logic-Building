#Write a program to flatten a nested list.

l=[[1,2],[2,3],[4,5],[6,7]]
flatten_=[]
for i in l:
    for j in i:
        flatten_.append(j)
print(flatten_)