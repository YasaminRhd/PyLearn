
def multiplication_table(n,m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            print( i * j , end=" ")
        print()

n = int(input("enter the number of columns: "))
m = int(input("enter the number of raws: "))
multiplication_table(n,m)