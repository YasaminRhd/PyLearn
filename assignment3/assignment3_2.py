import random
n = int(input("how many random numbers do you want to add in array?"))
array = []
for i in range (n):
    num = random.randint(1,100)
    if num != array:
        array.append(num)
print("the array is: ", array)