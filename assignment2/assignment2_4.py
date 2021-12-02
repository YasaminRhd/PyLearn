n = int(input("enter the number of all students: "))
grade = []
for i in range(n):
    grade.append(float(input("enter the grade: ")))
average = sum(grade) / n
min = min(grade)
max = max(grade)
print("the average is: ", average, "min is: ", min, "max is: ", max)