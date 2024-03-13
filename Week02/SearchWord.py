def myfunc():
    return


words = [input("Kindly enter 5 names of animals one at a time>>") for i in range(5)]
animals = sorted(words, key=str.lower)
print(f"The five names of animals you entered sorted alphabetically are {animals}")

UserSearch = input("Enter name of the animal to search>>")
if UserSearch in animals:
    print(f"{UserSearch} found")
else:
    print(f"{UserSearch} Not found")

myfunc()
