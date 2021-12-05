n = int(input("enter a number: "))
for i in range(int(n/2)):
    print("*", end="")
    print("#", end="")
if (n % 2) != 0:
    print("*")