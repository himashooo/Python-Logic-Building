#Merge two dictionaries.

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged=dict1 | dict2            #merge using '|'(dict2 overrides)
print(merged)