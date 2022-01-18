def sum(x, y):
    result = {}
    result['s'] = x['s'] + y['s']
    result['m'] = x['m'] + y['m']
    result['h'] = x['h'] + y['h']
    
    if ( result['s'] >= 60 ) :
        result['s'] -= 60
        result['m'] += 1
        
    if ( result['m'] >= 60 ) :
        result['m'] -= 60
        result['h'] += 1
        
    return result

def sub(x, y):
    result = {}
    result['s'] = x['s'] - y['s']
    result['m'] = x['m'] - y['m']
    result['h'] = x['h'] - y['h']
    
    if ( result['m'] < 0 ) :
        result['m'] += 60
        result['h'] -= 1
        
    if ( result['s'] < 0 ) :
        result['s'] += 60
        result['m'] -= 1
           
    return result


def SecondToTime(second):
    result = {}
    result['h'] = second // 3600
    second = second - (result['h'] * 3600)
    result['m'] = second // 60 
    result['s'] = second - (result['m'] * 60)
    
    return result

def timeToSecond(time):
    second = ( time['h'] * 3600 ) + ( time['m'] * 60 ) + ( time['s'] )
    return second

def show(x):
    print(x['h'], " : ", x['m'], " : ", x['s'])
    
print ('choice one of below')
print ('1.sum')
print ('2.sub')
print ('3.seconds to time')
print ('4.time to second')
choice = int(input('enter your choice: '))
  
match choice:
    case 1:
        data = input("enter the data in 00:00:00 form: ")
        splited = data.split(":")
        time1 ={}
        time1['h'] = int(splited[0])
        time1['m'] = int(splited[1])
        time1['s'] = int(splited[2])
        
        data = input("enter the data in 00:00:00 form: ")
        splited = data.split(":")
        time2 ={}
        time2['h'] = int(splited[0])
        time2['m'] = int(splited[1])
        time2['s'] = int(splited[2])
        
        sum = sum(time1, time2)
        print("the sum is: ", end='')
        show(sum)

    case 2:
        data = input("enter the data in 00:00:00 form: ")
        splited = data.split(":")
        time1 ={}
        time1['h'] = int(splited[0])
        time1['m'] = int(splited[1])
        time1['s'] = int(splited[2])
        
        data = input("enter the data in 00:00:00 form: ")
        splited = data.split(":")
        time2 ={}
        time2['h'] = int(splited[0])
        time2['m'] = int(splited[1])
        time2['s'] = int(splited[2])
        
        sub = sub(time1, time2)
        print("the sub is: ", end='')
        show(sub)        
        
    case 3:
        data = int(input("enter the data: "))
        time = SecondToTime(data)
        print('time: ', end='')
        show(time)
        
    case 4:
        data = input("enter the data in 00:00:00 form: ")
        splited = data.split(":")
        time ={}
        time['h'] = int(splited[0])
        time['m'] = int(splited[1])
        time['s'] = int(splited[2])
        seconds = timeToSecond(time)
        print('in seconds: ', seconds)