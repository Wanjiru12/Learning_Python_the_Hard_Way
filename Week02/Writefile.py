from sys import argv
script, filename = argv
print(f"We are going to erase{filename}")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
input("?")
print("Opening the file")
text = open(filename, 'w')
print("Truncating the file goodbye!!!")
text.truncate()
print("Kindly enter 3 lines")
line1 = input("Enter new message line1>")
line2 = input("Enter message for line2>")
line3 = input("Enter message for line3>")
print("The above text is going to be updated to the file")
text.write(line1)
text.write("\n")
text.write(line2)
text.write("\n")
text.write(line3)
text.write("\n")

print("Finally we close the file")
text.close()