import math

print("a Quadratic Equation: ax^2 + bx + c = 0. ")
a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))

delta = (b**2) - (4*a*c)

if delta > 0 :
    print("we get two real solutions")
    x1 = ((-b) + math.sqrt(delta))/ (2*a)    
    x2 = ((-b) - math.sqrt(delta))/ (2*a)
    print("x1 =", x1, " x2 =", x2)
    
if delta == 0 :
    print("we get just ONE solution")
    x = -b / 2*a
    print("x =", x)
    
if delta < 0 :
    print("we get complex solutions")