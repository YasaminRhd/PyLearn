a = int(input("enter the length of side a: "))
b = int(input("enter the length of side b: "))
c = int(input("enter the length of side c: "))

if (a + b > c ) and (b + c > a) and (a + c > b):
    print("this triangle can be formed")
else:
    print("this triangle can not be formed")