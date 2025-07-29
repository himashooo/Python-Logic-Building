import string
l="HelLO There,How are you!"
a="".join(ch for ch in l if ch not in string.punctuation and ch!=" ")
print(a)
upper=0
lower=0
for i in a:
    if i in a.lower():
        lower+=1
    else:
        upper+=1
print(f"upper={upper}\nlower={lower}")