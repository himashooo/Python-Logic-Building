a=int(input("enter no of rows"))
b=int(input("enter no of colums"))
matrix=[]
for i in range(a):
    row=[]
    for j in range(b):
        n=int(input(f"enter values for{[i]}{[j]}: "))
        row.append(n)
    matrix.append(row)
for i in matrix:
    print(i)