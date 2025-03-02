#1
import os
path = input()
print("Only directories:")
for name in os.listdir(path):
    if os.path.isdir(os.path.join(path, name)):  
        print(name)
print("\nOnly files:")
for name in os.listdir(path):
    if os.path.isfile(os.path.join(path, name)):  
        print(name)
print("\nAll directories and files:")
for name in os.listdir(path):
    print(name)

#2
import os
path = str(input())
x = os.access(path, os.F_OK)
print('Exist:', x)
x = os.access(path, os.R_OK)
print('Readable:', x)
x = os.access(path, os.W_OK)
print('Writable:', x)
x = os.access(path, os.X_OK)
print('Executable:', x)

#3
import os
path = str(input())
print("Exists: ")
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))
#4
with open("C:\Users\HP\Desktop\springpp2\lab6\file.txt") as file:
    lines = len(file.readlines())
    print('Total Number of lines:', lines)
#5
list = input().split(' ')
with open("C:\Users\HP\Desktop\springpp2\lab6\file.txt", "w") as file:
        for c in list:
                file.write("%s\n" % c)
x = open("C:\Users\HP\Desktop\springpp2\lab6\file.txt")
print(x.read())
#6
import string
import os
for letter in string.ascii_uppercase:
    x = letter + ".txt"
    with open("C:\Users\HP\Desktop\springpp2\lab6\file.txt" + x, "w") as file:
       file.writelines(letter)
#7
with open("C:\Users\HP\Desktop\springpp2\lab6\file.txt") as file:
    with open("C:\Users\HP\Desktop\springpp2\lab6\copy.txt", "w") as file1:
        for line in file:
            file1.write(line)

#8
import os
path = str(input())
if os.path.exists(path):
    os.remove(path)
else:
    print("No such file exists.")