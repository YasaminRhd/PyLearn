data = input("enter the data in 00:00:00 form: ")
splited = data.split(":")
seconds = (int(splited[0])*3600) + (int(splited[1])*60) + int(splited[2])
print(seconds)