def Checkered_page(n,m):
    
    for i in range(n):
        if i % 2 !=0:
            for i in range(m):
                if i % 2 != 0:
                    print("*", end="")
                else:
                    print("#", end="")
        if i % 2 == 0:
            for i in range(m):
                if i % 2 != 0:
                    print("#", end="")
                else:
                    print("*", end="")             
        print()

n = int(input("enter the number of columns: "))
m = int(input("enter the number of raws: "))

Checkered_page(n,m)