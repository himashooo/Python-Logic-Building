#Find the longest word in a sentence.

sentence=input("Enter your sentence")
words=sentence.split()          #split sentence into words
largest_=max(words ,key=len)    #find largest word using key=len
print(f"largest word is this entence is '{largest_}'")