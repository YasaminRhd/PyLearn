first_name = input("enter fist name: ")
last_name = input("enter last name: ")


grade1 = float(input("enter garde 1"))
grade2 = float(input("enter garde 2"))
grade3 = float(input("enter garde 3"))


average = ( grade1 + grade2 + grade3 ) / 3

if (average >= 17) :
    print("Great")
    
if (17 > average >= 12) :
    print("Normal")
    
if (average < 12) :
    print("Fail")
