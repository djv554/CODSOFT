#Design a simple calculator with basic arithmetic operations. Prompt the user to input two numbers and an operation choice. Perform the calculation and display the result.

def calculator():
 print("CALCULATOR")
 while(True):
    a=float(input("\nEnter the first number:"))
    b=float(input("Enter the second number:"))
    print("\nChoose the arithmetic operation to be performed between the two input numbers:")
    print("1.Addition(+)\n2.Subtraction(-)\n3.Multiplication(*)\n4.Division(/)\nAny other to exit")
    op=input("Your choice:")
    
    if op=='1':
        result=a+b
        print(f"\n{a} + {b} = {result}")
    elif op=='2':
        result=a-b
        print(f"\n{a} - {b} = {result}")
    elif op=='3':
        result=a*b
        print(f"\n{a} * {b} = {result}")
    elif op=='4':
        try:
            result=a/b
            print(f"\n{a} / {b} = {result}")
        except:
            print("Sorry! Cannot divide by zero")
    else:
        break   
        
calculator()