class time:

    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def sum(self, x):
        result = time(None, None, None)
        result.s = self.s + x.s
        result.m = self.m + x.m
        result.h = self.h + x.h

        if (result.s >= 60):
            result.s -= 60
            result.m += 1

        if (result.m >= 60):
            result.m -= 60
            result.h += 1

        return result

    def sub(self, x):
        result = time(None, None, None)
        result.s = self.s - x.s
        result.m = self.m - x.m
        result.h = self.h - x.h

        if (result.m < 0):
            result.m += 60
            result.h -= 1

        if (result.s < 0):
            result.s += 60
            result.m -= 1
            
        if (result.h < 0):
            print('choose your data wisely!')
        return result

    def SecondToTime(second):
        result = time(None, None, None)
        result.h = second // 3600
        second = second - (result.h * 3600)
        result.m = second // 60
        result.s = second - (result.m * 60)

        return result

    def timeToSecond(time):
        second = (time.h * 3600) + (time.m * 60) + (time.s)
        return second

    def show(self):
        print(self.h, " : ", self.m, " : ", self.s)


print('choose one of below')
print('1.sum')
print('2.sub')
print('3.seconds to time')
print('4.time to second')
choice = int(input('enter your choice: '))

match choice:
    case 1:
        data = input("enter the data in 00:00:00 form: ")
        splited = data.split(":")
        time1 = time(None, None, None)
        time1.h = int(splited[0])
        time1.m = int(splited[1])
        time1.s = int(splited[2])

        data = input("enter the data in 00:00:00 form: ")
        splited = data.split(":")
        time2 = time(None, None, None)
        time2.h = int(splited[0])
        time2.m = int(splited[1])
        time2.s = int(splited[2])

        sum = time1.sum(time2)
        print("the sum is: ", end='')
        sum.show()

    case 2:
        data = input("enter the data in 00:00:00 form: ")
        splited = data.split(":")
        time1 = time(None, None, None)
        time1.h = int(splited[0])
        time1.m = int(splited[1])
        time1.s = int(splited[2])

        data = input("enter the data in 00:00:00 form: ")
        splited = data.split(":")
        time2 = time(None, None, None)
        time2.h = int(splited[0])
        time2.m = int(splited[1])
        time2.s = int(splited[2])

        sub = time1.sub(time2)
        print("the sub is: ", end='')
        sub.show()

    case 3:
        data = int(input("enter the data: "))
        Time = time.SecondToTime(data)
        print('time: ', end='')
        Time.show()

    case 4:
        data = input("enter the data in 00:00:00 form: ")
        splited = data.split(":")
        Time = time(None, None, None)
        Time.h = int(splited[0])
        Time.m = int(splited[1])
        Time.s = int(splited[2])

        seconds = Time.timeToSecond()
        print('in seconds: ', seconds)
