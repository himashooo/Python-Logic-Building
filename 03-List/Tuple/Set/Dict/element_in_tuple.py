#Write a function to check if an element exists in a tuple.

l = ("Hey", "himanshu", "how", "are", "you", "they")
n="hey"             #string to search
if n.lower() in map(str.lower,l):
    print("present")
else:
    print("not present")