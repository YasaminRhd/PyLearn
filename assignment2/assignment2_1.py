num = []
while True:
    a = input("enter a number or exit: ")
    if a.isnumeric():
        num.append(int(a))
    elif a == "exit":
        _sum = sum(num)
        print("sum of the entered numbers are: ", _sum)
        break