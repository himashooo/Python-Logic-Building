#Create a set of unique characters from a string.

l="Himanshuu".lower()
a=set()
for i in l:
    if l.count(i)==1:       # check if character appears once
        a.add(i)
print(a)