#Create a function that accepts a string and returns it reversed

def rev_str(l):
    rev=""
    for i in l[::-1]: #reverse string
        rev+=i        #append each char
    return rev   
print(rev_str("HIMANSHU"))

                  #OR SIMPLER
"""def rev_str2(m):
    return m[::-1]
print(rev_str2("HIMANSHU"))"""