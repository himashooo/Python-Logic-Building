import string
par_="hello good evening"
par_new="".join([ch for ch in par_ if ch not in string.punctuation and ch!=" "])
freq={}
for i in par_new:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
for key_,value_ in freq.items():
    print(f"{key_}={value_}")