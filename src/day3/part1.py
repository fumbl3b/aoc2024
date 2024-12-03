import re

file = open('./input.txt', 'r')

# pattern = r'mul\(\d+,\d+\)'
pattern = r"(mul\(\d+,\d+\)|do\(\)|don't\(\))"


matches = re.findall(pattern, file.read())

print(matches)
numbers = []
do = True
for command in matches:
    if command == 'don\'t()':
        do = False
        continue
    if command == 'do()':
        do = True
        continue
    if do:
        hit_comma = False
        num1 = ''
        num2 = ''
        for char in list(command):
            if not hit_comma and char.isdigit():
                num1 += char
            elif char == ',':
                hit_comma = True
            elif hit_comma and char.isdigit():
                num2 += char
        numbers.append((int(num1), int(num2)))

print(numbers)

total = sum((n[0] * n[1]) for n in numbers)
print(total)
