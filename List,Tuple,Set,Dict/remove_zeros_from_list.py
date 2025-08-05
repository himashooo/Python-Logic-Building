#Write a program to remove all zeros from a list.

l=[1,2,3,0,4,0,6,0,0]
new_=[i for i in l if i!=0]     # keep non-zero values
print(new_)