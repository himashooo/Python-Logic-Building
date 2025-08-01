#Take a list of names and return only those starting with 'A'.

def a_name(lst):
    l1=[]
    for i in lst:
        if i.startswith("A"or"a"):
            l1.append(i)
    return l1
lst=["Himanshu","Akshat","Ankit","Arshdeep","Akhil","Sandeep","Abhi","Gaurav"]
print(a_name(lst))