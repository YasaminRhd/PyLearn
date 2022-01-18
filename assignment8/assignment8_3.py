n = int(input('enter a number: '))

min = 1
max = 2*n - 1
spaces = n -1
while ( min <= max ):
    print( " " * spaces + "*" * min)
    min += 2
    spaces -= 1
    
min = 1
max = 2*n - 1 - 2
i = 1
while ( max >= 1 ):
    print( " " * i + "*" * max)
    max -= 2
    i += 1    
