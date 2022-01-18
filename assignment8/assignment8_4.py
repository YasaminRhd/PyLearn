# The numerator is the top part of a fraction, and the denominator is the bottom part of a fraction.

# summation
def sum(x, y):
    result = {}
    result['n'] = x['n'] * y['d'] + x['d'] * y['n']
    result['d'] = x['d'] * y['d']
    return result

# subtraction
def sub(x, y):
    result = {}
    result['n'] = x['n'] * y['d'] - x['d'] * y['n']
    result['d'] = x['d'] * y['d']
    return result

# multiplication
def mul(x, y):
    result = {}
    result['n'] = x['n'] * y['n']
    result['d'] = x['d'] * y['d']
    return result

# division
def div(x, y):
    result = {}
    result['n'] = x['n'] / y['n']
    result['d'] = x['d'] / y['d']
    return result

def show(x):
    print(x['n'], '/', x['d'])
    
# a / b
print('fisrt fraction:')
n1 = int(input(" enter numerator: "))
d1 = int(input(" enter denominator: "))
fraction1 = { 'n' : n1, 'd': d1 }

# a / b
print('second fraction:')
n2 = int(input(" enter numerator: "))
d2 = int(input(" enter denominator: "))
fraction2 = { 'n' : n2, 'd': d2 }


sum = sum(fraction1, fraction2)
sub = sub(fraction1, fraction2)
mul = mul(fraction1, fraction2)
div = div(fraction1, fraction2)



print('summation : ', end='')
show(sum)

print('subtraction : ' , end='')
show(sub)

print('multiplication : ' , end='')
show(mul)

print('division : ' , end='')
show(div)
