n = int(input("tedade jomalat ra vared konid: "))

def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return(Fibonacci(n-1) + Fibonacci(n-2))

for x in range(1,n+1):
    print(Fibonacci(x), end=" ") 
