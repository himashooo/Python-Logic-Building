#Write a program to count vowels in a string.

a="himanshu"
count=0
for i in a.lower():     #convert to lowercase
    if i in "aeiou":
        count+=1
print(count)