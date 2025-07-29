sentence=input("Enter your sentence")
words=sentence.split()
largest_=max(words ,key=len)
print(f"largest word is this entence is '{largest_}'")