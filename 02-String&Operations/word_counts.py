import string  
def ct(n):
    n=n.replace(" ","")
    cleaned = ''.join(char for char in n if char not in string.punctuation)
    count=0
    for i in cleaned:
        count+=1
    return count
n="Hi himanshu how was you day,what are you doing now at this time of night.." \
"i am just solving some questions"
print(ct(n))