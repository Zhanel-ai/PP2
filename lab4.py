#Python iterators & generators

#1
def squares(N):
    for i in range(1, N + 1):
        yield i ** 2
for x in squares(6):
    print(x)


#2
def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i
n = int(input())
print(",".join(str(x) for x in even_numbers(n)))



#3
def div_3_and_4(n):
    for i in range(0, n + 1):
        if i % 12 == 0:
            yield i
print(list(div_3_and_4(60)))



#4
def squares(a, b):
    for x in range(a, b + 1):
        yield x * x
for values in squares(1, 9):
    print(values)



#5
def num_down(n):
    for x in range(n, -1, -1):
        yield x
print(list(num_down(10)))  







#Python date
from datetime import date, datetime, timedelta

#1
print(date.today() - timedelta(days=5))



#2
today = date.today()
print("yesterday:", today - timedelta(days=1))
print("today:", today)
print("tomorrow:", today + timedelta(days=1))



#3
now_no_micro = datetime.now().replace(microsecond=0)
print(now_no_micro)



#4
date1 = datetime(2025, 10, 9, 12, 0, 0)
date2 = datetime(2025, 10, 10, 12, 0, 0)

difference = (date2 - date1).total_seconds() 
print("Difference in seconds:", difference)







#Python Math library
import math

#1
def deg_to_rad(deg: float) -> float:
    return math.radians(deg)
print(deg_to_rad(15))  # 0.261799.....



#2
def trapezoid_area(h: float, a: float, b: float) -> float:
    return (a + b) * h / 2
print(trapezoid_area(5, 5, 6))  # 27.5



#3
n = int(input("Enter number of sides: "))     
s = float(input("Enter length of a side: "))  

area = (n * s ** 2) / (4 * math.tan(math.pi / n))

print("The area of the polygon is:", area)
#4 5 #25.00.....


#4
def parallelogram_area(base: float, height: float) -> float:
    return base * height
print(parallelogram_area(5, 6))  #30.0








#Python JSON parsing
import json

with open("sample-data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 30)
print("DN")
print("-" * 30)



for item in data.get("imdata", []):
    obj = next(iter(item.values()))
    attrs = obj.get("attributes", {})
    dn = attrs.get("dn", "")
    print(dn)
