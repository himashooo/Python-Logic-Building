#Use list comprehension to square all even numbers from 1 to 20.

square_=[i**2 for i in range(1,21) if i%2==0]
print(square_)