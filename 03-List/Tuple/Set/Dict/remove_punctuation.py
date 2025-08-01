#Remove punctuation from a sentence.

import string
l="Wait, is that your book -on my desk?"
l_new=""
for i in l:
    if i not in string.punctuation:
        l_new+=i
print(l_new)