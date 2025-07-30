#Create a program that checks if a string is an anagram of another

def anagram(str1,str2):
    if sorted(str1)==sorted(str2):          #sorted in alphabetic order/compare
        print(f"{str1},{str2} it is a anagram")
    else:
        print("not a anagram")
print(anagram("listen","silent"))