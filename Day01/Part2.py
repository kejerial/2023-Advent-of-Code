import re

file = open("/Users/kevinjeon/Code/2023 Advent of Code/Day01/input.txt", "r")
sum = 0
conv = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}

for line in file:
    for word in conv.keys():
        count = 0
        for m in re.finditer(word, line):
            line = line[:m.start()+count+1] + conv.get(word) + line[m.start()+1+count:]
            count += 1
    numbers = re.findall('\d', line)
    sum += int(numbers[0]) * 10 + int(numbers[-1])

print(sum)
