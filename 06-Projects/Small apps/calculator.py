#Basic Calculator

def calc(no1,no2,opr):
    try:
        if opr == "+":          #addition
            return no1+no2
        elif opr == "-":        #subtraction
            return no1-no2
        elif opr == "*":        #multiplication
            return no1*no2
        elif opr == "/":        #division
            return no1/no2
        else:
            print("Invalid operation")
    except ZeroDivisionError:
        return "Cannot divide by zero"
try:
    no1=int(input("enter no 1: "))
    no2=int(input("enter no 2: "))
    opr=input("enter the operation: ")
    print(calc(no1,no2,opr))
except ValueError:
    print(f"{ValueError} value error")
