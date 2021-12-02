second = int(input("enter the data: "))
def secondTohour(second):
    h = second // 3600
    second = second - (h * 3600)
    min = second // 60 
    second = second - (min * 60)
    return h,min,second
h, min, second = secondTohour(second)
print(h, ":", min, ":", second)