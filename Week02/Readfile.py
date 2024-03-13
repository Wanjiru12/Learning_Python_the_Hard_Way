from sys import argv
script, filename = argv
text = open(filename)
print(f"Here is your {filename}")
print(text.read())
print("type the file name again ")
file_again = input(">")
text_again = print(f"here is {file_again}")
text_display = open(file_again)
print(text_display.readline())
for x in text_display :
    print(x)
text.close()
text_display.close()

