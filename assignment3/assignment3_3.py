array = []
n = int(input("how many elements does the array have? "))
for i in range(n):
    num = int(input("enter element of the array: "))
    array.append(num)
print("entered array is: ", array)
sorted_array = sorted(array)
print( sorted_array )
if sorted_array == array:
    print("entered array is sorted")
else:
    print("entered array is not sorted")
    
    
    
# without using sorted 
array = []
n = int(input("how many elements does the array have? "))
for i in range(n):
    num = int(input("enter element of the array: "))
    array.append(num)
print("entered array is: ", array)
for i in range(1, len(a)):
    if a[i] < a[i-1]:
        print("entered array is not sorted")
        exit()
 print("entered array is sorted")
