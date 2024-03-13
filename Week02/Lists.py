students = list(("mary", "Alice", "James", "Janet"))
for x in students :
   print(x)
print(students[2])

if "Ann" in  students :
    print("yes mary is presnt")
else:print("Absent")

students.insert(0,"Lucy")
print(students)

students.append("Robert")
print(students)

New_joiners = ["Peter", "Anthony"]
students.extend(New_joiners)
print(students)
students.remove("Peter")
print(students)
students.pop(6)
print(students)

for i in range(len(students)) :
    print(students[i])

i=0
while i < len(students) :
    print(students[i])
    i = i+1

students.sort()
print(students)

students.sort(reverse = True)
print(students)