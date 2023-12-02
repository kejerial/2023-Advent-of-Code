import re

file = open("./Day01/input.txt", "r")

sum = 0

for line in file:
    numbers = re.findall('\d', line)
    sum += int(numbers[0]) * 10 + int(numbers[-1])

print(sum)