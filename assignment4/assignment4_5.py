from math import factorial, sqrt

user_input = int(input('enter your number: '))
flag = False

for i in range(int(sqrt(user_input)) + 1):
  if factorial(i) == user_input:
    print('your number is the factorial of: ', i)
    flag = True
if not flag:
  print('your number is not a factorial of any number.')