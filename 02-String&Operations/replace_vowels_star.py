#Replace all vowels in a string with '*'.

l="hello himanshu how are you"
vowels="aAeEiIoOuU"
new_=""
for i in l:         #replace vowels with "*"
    if i in vowels:
        new_+="*"
    else:
        new_+=i
print(new_)