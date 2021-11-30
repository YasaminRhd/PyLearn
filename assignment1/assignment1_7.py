import math 
print("This calculator support these kind of operators: +, -, *, /, sin, radical, cos, cot, tan, factorial.")
op = input("Please enter desired mathematician operator: ")

if op == "+" or op == "-" or op == "*" or op == "/":
    num1 = float(input("Please enter first number: "))
    num2 = float(input("Please enter second number: "))

    if op == "+":
        result = num1 + num2
    
    if op == "-":
        result = num1 - num2
        
    if op == "*":
        result = num1 * num2
        
    if op == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Can't divide by zero!"
else:          
    num = float(input("Please enter a number: "))
    
    if op == "radical":
        if ( num ) < 0:
            print("square root of a negative number does not exist!")
        else:
            result = math.sqrt(num)
            
    if op == "factorial":
        result = math.factorial(int(num))
    
    if op == "sin":
        a = input("did you enter the data in radian? (type yes or no) " )
        if a == "yes":
            result = math.sin(math.degrees(num))
        else:
            result = math.sin(num)
        
    if op == "cot":
        a = input("did you enter the data in radian? (type yes or no) " )
        if a == "yes":
            result = math.cot(math.degrees(num))
        else:
            result = math.scot(num)
        
    if op == "cos":
        a = input("did you enter the data in radian? (type yes or no) " )
        if a == "yes":
            result = math.cos(math.degrees(num))
        else:
            result = math.cos(num)
        
    if op == "tan":
        a = input("did you enter the data in radian? (type yes or no) " )
        if a == "yes":
            result = math.tan(math.degrees(num))
        else:
            result = math.tan(num)
        
print("The result is: ", result)