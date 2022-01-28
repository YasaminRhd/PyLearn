# The numerator is the top part of a fraction, and the denominator is the bottom part of a fraction.

class fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    # summation
    def sum(self, x):
        result = fraction(None, None)
        result.num = x.num * self.den + x.den * self.den
        result.den = x.den * self.den
        return result

    # subtraction
    def sub(self, x):
        result = fraction(None, None)
        result.num = x.num * self.den - x.den * self.den
        result.den = x.den * self.den
        return result

    # multiplication
    def mul(self, x):
        result = fraction(None, None)
        result.num = x.num * self.num
        result.den = x.den * self.den
        return result
    
    # division
    def div(self, x):
        result = fraction(None, None)
        result.num = x.num / self.num
        result.den = x.den / self.den
        return result

    def show(self):
        print( self.num, '/', self.den )

print('fisrt fraction:')        
a = fraction( int(input('enter the numerator: ')), int(input('enter the denominator: ')) )     
print('second fraction:')
b = fraction( int(input('enter the numerator: ')), int(input('enter the denominator: ')) )     

sum = a.sum(b)
sub = a.sub(b)
mul = a.mul(b)
div = a.div(b)

print('summation : ', end='')
sum.show()

print('subtraction : ' , end='')
sub.show()

print('multiplication : ' , end='')
mul.show()

print('division : ' , end='')
div.show()