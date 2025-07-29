#Count capital and lowercase letters in a string.

import string
l="HelLO There,How are you!"
a="".join(ch for ch in l if ch not in string.punctuation and ch!=" ")       #remove punctuations and spaces
print(a)
upper=0
lower=0
for i in a:                 #count upper and lowercase char
    if i.islower():
        lower+=1
    elif i.isupper():
        upper+=1
print(f"upper={upper}\nlower={lower}")