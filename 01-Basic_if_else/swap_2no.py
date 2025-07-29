#Swap two numbers without using a third variable.

a=2
b=3
print(f"Before swap a= {a}, b= {b}")

a=a+b
b=a-b
a=a-b
print(f"After swap a= {a}, b= {b}")