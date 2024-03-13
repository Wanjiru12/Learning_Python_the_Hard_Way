print('What is you name?'),
name = input()
print("What is your age?"),
age = input()
print("What is your weight?"),
weight = input()

intro = "My name is {} I am, {} and my weight is {}"
print(intro.format(name, age, weight))

sum = int(age)+float(weight)
print(sum)

# Prompting Users
name = input("What is your name")
school = input("which high school did you attend?")

pdetails = "My name is {}, I go to {} school"
print(pdetails.format(name, school))