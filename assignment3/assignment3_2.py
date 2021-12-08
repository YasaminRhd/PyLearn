import random
n = int(input("how many random numbers do you want to add in array?"))
array = []
while (len(array) != n):
    num = random.randint(1,100)
    if num not in array:
        array.append(num)
print("the array is: ", array)
