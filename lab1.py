print("Hello, World!")


if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 



#This is a comment




"""
This is a comment
written in
more than just one line
"""


x = 5
y = "John"
print(x)
print(y)



x = 4       
x = "Sally"
print(x)



x = str(3)    
y = int(3)    
z = float(3) 
print(x)
print(y)
print(z)



x = 5
y = "John"
print(type(x))
print(type(y))



x = "John"
print(x)
x = 'John'
print(x)



a = 4
A = "Sally"

print(a)
print(A)



myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)




myVariableName = "John"   #Camel Case
MyVariableName = "John"   #Pascal Case
my_variable_name = "John"   #Snake Case




x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)



x = y = z = "Orange"
print(x)
print(y)
print(z)



fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)



x = "Python is awesome"
print(x)



x = "Python"
y = "is"
z = "awesome"
print(x, y, z)



x = "Python "
y = "is "
z = "awesome"
print(x + y + z)



x = 5
y = 10
print(x + y)



x = 5
y = "John"
print(x, y)



x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()



x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)




def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)




x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)




x = 5
print(type(x))





x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))





x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))






x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))





x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))





x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))






x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))





import random

print(random.randrange(1, 10))





x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3




x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2





x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'





print("Hello")
print('Hello')




print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')



a = "Hello"
print(a)






a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)




a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)




a = "Hello, World!"
print(a[1])




for x in "banana":
  print(x)





a = "Hello, World!"
print(len(a))




txt = "The best things in life are free!"
print("free" in txt)




txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")





txt = "The best things in life are free!"
print("expensive" not in txt)




txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")




b = "Hello, World!"
print(b[2:5])
#llo





b = "Hello, World!"
print(b[:5])
#Hello




b = "Hello, World!"
print(b[2:])
#llo, World!



b = "Hello, World!"
print(b[-5:-2])
#orl



a = "Hello, World!"
print(a.upper())
#HELLO, WORLD!



a = "Hello, World!"
print(a.lower())
#hello, world!



a = " Hello, World! "
print(a.strip()) 
#"Hello, World!"




a = "Hello, World!"
print(a.replace("H", "J"))
#Jello, World!



a = "Hello, World!"
print(a.split(",")) 
#['Hello', ' World!']




a = "Hello"
b = "World"
c = a + b
print(c)
#HelloWorld




a = "Hello"
b = "World"
c = a + " " + b
print(c)
#Hello World




age = 36
txt = f"My name is John, I am {age}"
print(txt)
#My name is John, I am 36




price = 59
txt = f"The price is {price} dollars"
print(txt)
#The price is 59 dollars




price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
#The price is 59.00 dollars





txt = f"The price is {20 * 59} dollars"
print(txt)
#The price is 1180 dollars





txt = "We are the so-called \"Vikings\" from the north."
print(txt) 
#We are the so-called "Vikings" from the north.
