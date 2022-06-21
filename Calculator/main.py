##Calculator
from art import logo
#add
def add(n1, n2):
    return n1+n2
#subtract
def subtract(n1,n2):
    return n1-n2

#multiply
def multiply(n1, n2):
    return n1*n2

#divide
def divide(n1, n2):
    return n1/n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
     "/":divide
 }
def calculator():
    print(logo)
    morecalcs=True
    
    num1=float(input("What's the first number?"))
    while morecalcs==True:
        
        for operand in operations:
            print(operand)   
        operand=input("Which operation would you like to use")
        num2=float(input("What's the second number?"))
        
        calculations=operations[operand]
        answer = calculations(num1, num2)
        
        print (f"{num1} {operand} {num2} = {answer}")
       
        cont=input("Would you like to continue? Type y to continue or n to start a new calculation")
        if cont=="n":
            morecalcs=False
            calculator()
        else:
            num1=answer

calculator()