#Python builtin functions
#1
import math

numbers = input()
numbers = [int(x) for x in numbers.split()]

print(math.prod(numbers))




#2
def count_upper_lower(s):
    upper = sum(1 for ch in s if ch.isupper())
    lower = sum(1 for ch in s if ch.islower())
    return upper, lower

text = "Hello World"
print(count_upper_lower(text))  # (2, 8)




#3
def is_palindrome(text):
    if text == text[::-1]:
        print("Yes")
    else:
        print("No")

word = input("Word: ")
is_palindrome(word)




#4
import time
import math

num = int(input("Number: "))
ms = int(input("Ms: "))

time.sleep(ms / 1000)
result = math.sqrt(num) 
print(f"Square root of {num} after {ms} milliseconds is {result}")




#5
values = input().split()

bool_values = [x == "True" for x in values]

if all(bool_values):
    print("All of them are True")
else:
    print("At least one is False")




#Python Directories and Files
#1
import os

path = input("Path: ")

print("\nDirectories:")
for name in os.listdir(path):
    if os.path.isdir(os.path.join(path, name)):
        print(name)

print("\nFiles:")
for name in os.listdir(path):
    if os.path.isfile(os.path.join(path, name)):
        print(name)




#2
import os

path = input("Path: ")

print("Exists:", os.path.exists(path))
print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
print("Executable:", os.access(path, os.X_OK))




#3
import os

path = input("Path: ")

if os.path.exists(path):
    print("Path exists ")
    print("Directory:", os.path.dirname(path))
    print("Filename:", os.path.basename(path))
else:
    print("Path does not exist ")




#4
filename = input("Filename: ")

with open(filename, 'r') as f:
    lines = f.readlines()

print("Len:", len(lines))




#5
my_list = ['apple', 'banana', 'cherry']

with open('fruits.txt', 'w') as f:
    for item in my_list:
        f.write(item + '\n')

print("List written to fruits.txt")




#6
import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}.txt\n")

print("26 files created (A.txt to Z.txt)")




#7
source = input("File1: ")
destination = input("File2: ")

with open(source, 'r') as src:
    with open(destination, 'w') as dest:
        dest.write(src.read())

print(f"Copied content from {source} to {destination}")




#8
import os

path = input("Path to delete: ")

if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted")
    else:
        print("Not deleted")
else:
    print("File does not exist ")

