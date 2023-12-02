# Day 02 - Cube Conundrum
import re

file = open('./Day02/input.txt', 'r')
sum = 0

pattern = re.compile('\d+')
for line in file:
    games_string = line.split(':')[1]
    game_id = (line.split(':')[0]).split()[1]
    valid = True
    
    for m in pattern.finditer(games_string):
        ind = m.span()[1]
        char = games_string[ind + 1]
        if char == 'r' and int(m.group()) > 12:
                valid = False
        if char == 'g' and int(m.group()) > 13:
                valid = False
        if char == 'b' and int(m.group()) > 14:
                valid = False

    if (valid):
        sum += int(game_id)
        
print(sum)