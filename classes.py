#1
class MyString:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("String:")

    def printString(self):
        print(self.text.upper())




#2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2




#3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width




#4
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)




#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit: {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw: {amount}. Balance: {self.balance}")
        else:
            print("Insufficient funds!")





#6
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

nums = [1, 2, 3, 4, 5, 6, 7, 11, 13, 15, 17, 20]
primes = list(filter(lambda x: is_prime(x), nums))
print("Primes:", primes)