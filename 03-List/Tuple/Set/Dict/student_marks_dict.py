#Create a program to input and store student marks in a dictionary.

marks={}
a=int(input("enter no of students"))
for i in range (a):
    name_=input(f"Enter name of student{i+1}")
    n=float(input(f"Enter marks of student{i+1}"))
    marks[name_]=n
print(marks)
for x,y in marks.items():
    print(f"{x}:{y}")