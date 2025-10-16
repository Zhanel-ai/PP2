#1
import re

text = input("string: ")
pattern = r'ab*'
print("Match!" if re.fullmatch(pattern, text) else "No match")



#2
import re

text = input("string: ")
pattern = r'ab{2,3}'
print("Match!" if re.fullmatch(pattern, text) else "No match")



#3
import re

text = input("string: ")
pattern = r'[a-z]+_[a-z]+'
print(re.findall(pattern, text))



#4
import re

text = input("string: ")
pattern = r'[A-Z][a-z]+'
print(re.findall(pattern, text))



#5
import re

text = input("string: ")
pattern = r'^a.*b$'
print("Match!" if re.fullmatch(pattern, text) else "No match")



#6
import re

text = input("string: ")
pattern = r'[ ,.]'
print(re.sub(pattern, ':', text))



#7
import re

text = input("snake_case: ")
camel = re.sub(r'_([a-z])', lambda x: x.group(1).upper(), text)
print(camel)



#8
import re

text = input("string: ")
print(re.findall(r'[A-Z][a-z]*', text))



#9
import re

text = input("camelCase: ")
print(re.sub(r'([a-z])([A-Z])', r'\1 \2', text))



#10
import re

text = input("camelCase: ")
snake = re.sub(r'([A-Z])', r'_\1', text).lower().lstrip('_')
print(snake)




