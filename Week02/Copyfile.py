from sys import argv
from os.path import exists
script, from_file, to_file = argv
print(f"Copying files from{from_file} to {to_file}")
in_file = open(from_file)
indata = in_file.read()
print(f"{indata}")
print(f"The file to be copied is {len(indata)}bytes long")
print(f"Does the output file exists? {exists(to_file)} ")
print("Ready? Hit RETURN to continue, or click ctrl-C to abort")
input(">")
out_file = open(to_file, 'w')
out_file.write(indata)
print("File copied successfully thank you!!")
in_file.close()
out_file.close()
