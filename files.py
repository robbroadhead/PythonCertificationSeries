# Examples of files functions read(), readinto(), readline(), write(), close()
import os

print("Read in a file")

f = open("README.md", "r", encoding="utf-8")

line = f.readline()
while line != '':
    print(line)
    line = f.readline()


f.close()
f = open("README.md", "r")
print("Read in a file 15 char at a time")
line = f.readline(15)
while line != '':
    print(line)
    line = f.readline(15)


f.close()
f = open("README.md", "r")
print("Read complete file")
line = f.read()
print(line)

f.close()

print("Create a simple file")
f = open("test.txt", "w", encoding="utf-8")
f.write("This is a line\n")
f.write("This is a second line\n")
f.close()

print("Append to simple file")
f = open("test.txt", "a", encoding="utf-8")
f.write("This is a line\n")
f.write("This is a second line\n")
f.close()

f = open("README.md", "rb")
line = f.readline()
print(line)

print("Create a simple binary file")
f = open("test.txt", "wb")
temp = b'This is a line\n'
f.write(temp)
temp = b'This is a second line\n'
f.write(temp)
f.close()

print("Create a simple binary file")
f = open("test.txt", "wb")
temp = 68
f.write(temp.to_bytes(2,"big"))
f.close()

filename = "test.txt"
buffer = bytearray(os.path.getsize(filename))
with open(filename, 'rb') as f:
    f.readinto(buffer)
print(buffer)