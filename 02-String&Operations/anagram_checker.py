def anagram(str1,str2):
    if sorted(str1)==sorted(str2):          #sorted in alphabetic order/compare
        return str1 ,str2,"it is a anagram"
    else:
        return "not a anagram"
print(anagram("listen","silent"))