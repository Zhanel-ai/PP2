#1
def grams_to_ounces(grams: float) -> float:
    return 28.3495231 * grams

# print(grams_to_ounces(10))



#2
def f_to_c(f: float) -> float:
    return (5 / 9) * (f - 32)

# print(f_to_c(212))  



#3
def solve(numheads: int, numlegs: int):
    # c = chickens, r = rabbits
    # c + r = numheads
    # 2c + 4r = numlegs
    r = (numlegs - 2 * numheads) // 2
    c = numheads - r
    if r < 0 or c < 0 or 2*c + 4*r != numlegs:
        return None  
    return c, r

# print(solve(35, 94))



#4
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def filter_prime(nums):
    return list(filter(is_prime, nums))

# print(filter_prime([1,2,3,4,5,6,7,11,13,15,17,20]))



#5
from itertools import permutations

def print_permutations(s: str) -> None:
    for p in permutations(s):
        print(''.join(p))

# print_permutations("abc")



#6
def reverse_words(sentence: str) -> str:
    return ' '.join(sentence.split()[::-1])

# print(reverse_words("We are ready")) 



#7
def has_33(nums) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# print(has_33([1, 3, 3]))      
# print(has_33([1, 3, 1, 3]))   
# print(has_33([3, 1, 3]))     




#8
def spy_game(nums) -> bool:
    target = [0, 0, 7]
    idx = 0
    for x in nums:
        if x == target[idx]:
            idx += 1
            if idx == 3:
                return True
    return False

# print(spy_game([1,2,4,0,0,7,5]))  
# print(spy_game([1,0,2,4,0,5,7])) 
# print(spy_game([1,7,2,0,4,5,0]))  



#9
import math

def sphere_volume(r: float) -> float:
    return (4/3) * math.pi * r**3

# print(sphere_volume(1)) 




#10
def unique_list(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result

# print(unique_list([1,2,2,3,1,4,3]))  




#11
def is_palindrome(text: str) -> bool:
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

# print(is_palindrome("madam"))                
# print(is_palindrome("A man, a plan, a canal: Panama")) 




#12
def histogram(ints):
    for n in ints:
        print('*' * n)





#13
import random

def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    secret = random.randint(1, 20)
    tries = 0
    while True:
        guess = int(input("Take a guess.\n"))
        tries += 1
        if guess < secret:
            print("\nYour guess is too low.\nTake a guess.")
        elif guess > secret:
            print("\nYour guess is too high.\nTake a guess.")
        else:
            print(f"\nGood job, {name}! You guessed my number in {tries} guesses!")
            break

# guess_the_number()

