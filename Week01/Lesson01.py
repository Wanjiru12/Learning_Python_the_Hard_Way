#Hello Python
print("Hello World")
print((100-9)+78*23/ 89)

#Strings
values_list=["Orange", 1000, "Cherry", 76]
x, y, z, k = values_list
print(x)
print(y)
print(z)
#y="apple"
print(k)
print(int(y)/int(k))

#String Modification
print(2**8)
print("Cate's Laptop")
print('Cate\'s "Logo"')
print('Cate'+'mwai')
print(10*"cate")
print("cate\nmwai")
print(r"cate\nmwai"

##Variables
x=int(5)
y=float(4)
z=x+y
print(z)
print(x)
print(y)
print(23+z)
fname=str('Jane')
lname=str(' Ben')
print(fname + lname)
print(fname[0])
print(lname[-3])
print(fname[0:2])
print(lname+'son')
print(fname[0:3]+"nse")
len(fname)
type(lname)

#print Random Number
import random
print(random.randrange(11, 30))

#global variables
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

def myfunc2():
  x = "fantastic2"
  print("Python is " + x)


print(x)
myfunc2()
myfunc()

##Strings
a = "Hello, World!"
print(a[6])
for x in "learn":
    print(x)

x=(1,2,3,4,5,0)
print(len(x))

for i in x:
  print(i)

text=("Learning is needs effort you have to be consistent")
print("today" in text)
print("Effort" not in text)
if "Effort" in text:
  print("Yes,is present.")
else:
  print("Absent")

#split
a = "Hello, World!"
print(a.split()) # returns ['Hello', ' World!']

#concatenate
a="today"
b="is"
c="Thursday"
d=a+" "+b +" "+c
print(d)

#Format String
age=12
school="Nairobi School"
pet="cats"

Intro="My name is Ann, I am {0} years old, I go to school at {1}. I love {2}"
print(Intro.format(age, school, pet))

elson = "\tNelson Rolihlahla Mandela was a \"South African\"\n anti-apartheid activist and politician who\n served as the first president of South Africa\n from 1994 to 1999. He was the country's first black head\n of state and the first elected in a full\n representative democratic election."

print(Nelson)

#Methods
text="Hello World"
print(text.encode())
print(text.endswith(text))
print(text.find(text))

#Boolean
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
bool()

#Boolean Function
def myFunction() :
  return False

if myFunction() :
  print("This is true")
else: print("This False")

#datat type
x = 200
print(isinstance(x, float))

#List
students=["Jane", "Mary", "Jim", "Juma"]
print(students)
print(type(students))
Grades=list((23,74,12,90))
print(Grades)
print(type(Grades))
