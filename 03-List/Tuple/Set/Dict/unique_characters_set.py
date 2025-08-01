#Create a set of unique characters from a string.

l="Himanshuu".lower()
a=set()
for i in l:
    if l.count(i)==1:
        a.add(i)
print(a)