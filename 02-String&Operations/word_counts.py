#Count words in a sentence.

import string  
def ct(n):
    n=n.replace(" ","")         #remove all spaces
    cleaned = ''.join(char for char in n if char not in string.punctuation)     #remove punctuation
    count=0
    for i in cleaned:
        count+=1
    return count
n="Hi himanshu how was you day,what are you doing now at this time of night.." \
"i am just solving some questions"
print(ct(n))