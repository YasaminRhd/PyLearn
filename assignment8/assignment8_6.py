# summation 
def sum(x, y):
    result = {}
    result['r'] = x['r'] + y['r']
    result['i'] = x['i'] + y['i']
    return result

# subtraction
def sub(x, y):
    result = {}
    result['r'] = x['r'] - y['r']
    result['i'] = x['i'] - y['i']
    return result

# multiplication
def mul(x, y):
    result = {}
    result['r'] = ( x['r'] * y['r'] ) - ( x['i'] * y['i'] )
    result['i'] = ( x['i'] * y['r'] ) + ( x['r'] * y['i'] )
    return result

def show(x):
    print(x['r'] , ' + ', x['i'], 'i' )
    
# a + bi
print('fisrt complex number: ')
a1 = int(input(" enter a: "))
b1 = int(input(" enter b: "))
complex1 = { 'r' : a1, 'i': b1 }

# a + bi
print('second complex number: ')
a2 = int(input(" enter a: "))
b2 = int(input(" enter b: "))
complex2 = { 'r' : a2, 'i': b2 }


sum = sum(complex1, complex2)
sub = sub(complex1, complex2)
mul = mul(complex1, complex2)



print('summation : ', end='')
show(sum)

print('subtraction : ' , end='')
show(sub)

print('multiplication : ' , end='')
show(mul)