#Create a matrix using nested loops and fill it row-wise.

n=int(input("Enter no of rows: "))
m=int(input("enter no of columns: "))
matrix={}           #dict to store matrix

for i in range(n):
    for j in range(m):
        val_=int(input(f"enter the value in ({i},{j}): "))
        matrix[i,j]=val_
for i in range(n):
    for j in range(m):
        print(matrix[i,j],end="  ")         #print row wise
    print()