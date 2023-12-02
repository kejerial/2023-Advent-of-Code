# Day 02 - Cube Conundrum
import re

file = open('./Day02/input.txt', 'r')
sum = 0

pattern = re.compile('\d+')
for line in file:
    games_string = line.split(':')[1]

    min_cubes = [1, 1, 1]
    
    for m in pattern.finditer(games_string):
        ind = m.span()[1]
        char = games_string[ind + 1]
        if char == 'r' and int(m.group()) > min_cubes[0]:
                min_cubes[0] = int(m.group())
        if char == 'g' and int(m.group()) > min_cubes[1]:
                min_cubes[1] = int(m.group())
        if char == 'b' and int(m.group()) > min_cubes[2]:
                min_cubes[2] = int(m.group())

    sum += min_cubes[0] * min_cubes[1] * min_cubes[2]
        
print(sum)